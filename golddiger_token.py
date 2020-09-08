
import click

from datetime import datetime
from hashlib import sha256

DEFAULT_USER = 'amis'
DEFAULT_PASSWD = 'amis00'
TS = datetime.now().isoformat(timespec='seconds')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--user', type=str, default=DEFAULT_USER, show_default=True, help="User login")
@click.option('-p', '--password', type=str, default=DEFAULT_PASSWD, show_default=True, help="User password")
@click.option('--output-format', 'output_format', type=click.Choice(['url', 'detail', 'hash'], case_sensitive=False), default='URL', help="Generated token output format")
def cli(user, password, output_format):
    """
    GoldDigger Token generation tool.
    """

    m = sha256()
    m.update(user.encode())
    m.update(TS.encode())
    m.update(password.encode())

    if output_format == "url":
        print(f"login={user}&ts={TS}&hash={m.hexdigest()}")
    elif output_format == "detail":
        print(f"login={user}")
        print(f"ts={TS}")
        print(f"hash={m.hexdigest()}")
    elif output_format == "hash":
        print(f"hash={m.hexdigest()}")


if __name__ == "__main__":
    cli()
