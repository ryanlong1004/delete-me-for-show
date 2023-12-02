""" 
Convenience executor
"""

import subprocess
import click

def run(cmd):
    return subprocess.run(cmd.split(), shell=True, check=True)

@click.command
def test():
    """run testing suites"""
    return run("pytest")

@click.command
@click.option('--port', default=8000, help='specify a port number')
def serve(port=8000):
    """spins up a development server"""
    return run(f"python3 -m http.server {port}")

@click.group()
def cli():
    pass

cli.add_command(test)
cli.add_command(serve)

if __name__ == "__main__":
    cli()