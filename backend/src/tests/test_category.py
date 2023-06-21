from src.domain.entities.Category import Category
from src.domain.gates.CategoryFactory import CategoryFactory
from src.domain.services.MakeCategory import MakeCategory
from src.domain.services.RetrieveCategories import RetrieveCategories
from src.domain.gates.dto.RetrieveCategoriesDTO import RetrieveCategoriesDTO
from src.adapters.SqlAdapter import SqlAdapter
import pytest

def test_create_category() -> None:
    category = Category("Test", "Description test", "11111111111",0)
    assert category.name == "Test"
    assert category.description == "Description test"
    assert category.user_cpf == "11111111111"
    assert category.color == "F7BC0A"

def test_make_category_factory() -> None:
    obj = {
        "name": "Test",
        "description": "Description test",
        "color": "F7BC0A",
        "user_cpf": "11111111111"
    }
    category = CategoryFactory().make(obj)
    assert category.name == "Test"
    assert category.description == "Description test"
    assert category.user_cpf == "11111111111"
    assert category.color == "F7BC0A"
    
def test_should_not_make_category_factory_without_keys() -> None:
    obj = {
        "color": "F7BC0A",
    }
    with pytest.raises(TypeError) as e:
        CategoryFactory().make(obj)

def test_make_category(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(SqlAdapter, "AddCategory", lambda x, y: None)
    category = Category("Test", "Description test", "11111111111",0)
    res = MakeCategory(SqlAdapter()).make(category)
    assert res == "The category was successfully added."

def test_retrieve_category(monkeypatch: pytest.MonkeyPatch) -> None:
    category = Category("Test", "Description test", "11111111111",0)
    monkeypatch.setattr(SqlAdapter, "RetrieveCategoriesFromUser", lambda x, y: [category])
    category = RetrieveCategories(SqlAdapter()).make("11111111111")
    assert category[0].name == "Test"
    assert category[0].description == "Description test"
    assert category[0].user_cpf == "11111111111"
    assert category[0].color == "F7BC0A"

def test_retrieve_category_dto() -> None:
    category = Category("Test", "Description test", "11111111111",0)
    obj = RetrieveCategoriesDTO().make([category])
    assert obj["Categories"][0]["Name"] == "Test"
    assert obj["Categories"][0]["Description"] == "Description test"
    assert obj["Categories"][0]["User CPF"] == "11111111111"
    assert obj["Categories"][0]["Color"] == "F7BC0A"
    assert obj["Categories"][0]["Id"] == 0
    
