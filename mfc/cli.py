import typer

app = typer.Typer()

@app.command()
def mfc(millenium_falcon_file : str, empire_file : str):
    print('debug')