
import json
import asyncio

import click

import yaml as _yaml

from kong.client import Kong, KongError
from kong.components import KongEntity


@click.command()
@click.option(
    '--yaml', type=click.File('r'),
    help='Yaml configuration to upload'
)
@click.pass_context
def kong(ctx, yaml):
    return asyncio.get_event_loop().run_until_complete(_run(ctx, yaml))


def dump_kong_entity(obj):
    if isinstance(obj, KongEntity):
        return obj.data
    return obj


async def _run(ctx, yaml):
    async with Kong() as cli:
        if yaml:
            try:
                result = await cli.apply_json(_yaml.load(yaml))
                click.echo(
                    json.dumps(result, indent=4, default=dump_kong_entity)
                )
            except KongError as exc:
                raise click.ClickException(str(exc))
        else:
            click.echo(ctx.get_help())


def main():     # pragma    nocover
    kong()