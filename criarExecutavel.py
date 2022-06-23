import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="missao_impossivel_game.py", icon="assets/images/missao_impossivel_ico.ico"
)]


cx_Freeze.setup(
    name="Missão Impossível - Patrick",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["assets"]}},
    executables=arquivo
)