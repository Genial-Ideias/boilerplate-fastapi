from typer.testing import CliRunner

runner = CliRunner()

def test_create_user_cli(cli_app):
    result = runner.invoke(
        cli_app,
        ['users', 'create'],
        input='Leonardo Freitas\nleo@genialideias.com\nleo123321\n'
    )

    assert result.exit_code == 0
    assert 'Usuário cirado com sucesso!' in result.stdout
