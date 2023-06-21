from src.domain.entities.User import User

def test_create_user() -> None:
    user = User('11111111111', 'Test', 'test@test.com')
    assert user.cpf == '11111111111'
    assert user.name == 'Test'
    assert user.email == 'test@test.com'