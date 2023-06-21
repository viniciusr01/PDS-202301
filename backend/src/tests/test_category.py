from src.domain.entities.Category import Category

def test_create_category() -> None:
    category = Category("Test", "Description test", "11111111111",0)
    assert category.name == "Test"
    assert category.description == "Description test"
    assert category.user_cpf == "11111111111"
    assert category.color == "F7BC0A"