from cx_Freeze import setup, Executable

executables = [Executable('./RaidBotSource.py')]

setup(name='RaidBot',
      version='3.0',
      description='VK Raid Bot created by Victor-web-dot',
      executables=executables)
