#! env python3

import os
import subprocess

import click
import yaml

ALL_STEPS = ['pre_build', 'build', 'pre_deploy', 'deploy', 'clean']


def get_app_config(app):
    try:
        with open(f"{app}/.roost.yaml") as f:
            return yaml.load(f, Loader = yaml.FullLoader)
    except:
        ctx = click.get_current_context()
        click.echo('Could not load application configuration. Make sure the application directory contains a .roost.yaml file.')
        click.echo(ctx.get_help())
        ctx.exit()


def goto_app(app):
    try:
        os.chdir(app)
        click.echo(f'Currently working in {os.getcwd()}')
    except:
        click.echo(f'Could not change working directory to {app}')
        click.exit()


def set_step_env(step_envs={}):
    for env in step_envs.items():
        [name, val] = env
        os.environ[name] = val
        subprocess.run(['echo', name, os.environ[name]])


def run_step_execs(step_execs=[]):
    for step in step_execs:
        split_step = step.split()
        subprocess.run(split_step)


def run_step_scripts(step_scripts=[]):
    for step in step_scripts:
        if step.startswith('./'):
            split_step = step.split()
        else:
            split_step = f"./{step}".split()
        subprocess.run(split_step)


def run_entire_step(step, skip_env):
    if skip_env:
        pass
    else:
        set_step_env(step.get('env', {}))
    run_step_execs(step.get('exec', []))
    run_step_scripts(step.get('script', []))


@click.command()
@click.version_option('0.0.1')
@click.option('--app', help='Path to the app you want to operate.')
@click.option('--full', default=False, is_flag=True, help='Run all commands for the operating app.')
@click.option('--build', flag_value='build', help='Run build command for the operating app')
@click.option('--deploy', flag_value='deploy', help='Run deploy command for the operating app')
@click.option('--clean', flag_value='clean', help='Run deploy command for the operating app')
@click.option('--skip-env', flag_value=True, help='Skip environmental variable assignment for the operating app')
@click.option('--env', '-e', help='Provide environment variables for the operating app in the format: ENV=myenv', multiple=True)
def main(app, full, build, deploy, clean, skip_env, env):
    config = get_app_config(app)
    goto_app(app)
    if len(env):
        for env_item in env:
            [name, val] = env_item.split('=')
            os.environ[name] = val

    if full:
        for step in ALL_STEPS:
            run_entire_step(config.get(step, {}), skip_env)
    else:
        build_step = config.get(build)
        if build_step:
            run_entire_step(build_step, skip_env)

        deploy_step = config.get(deploy)
        if deploy_step:
            run_entire_step(deploy_step, skip_env)

        clean_step = config.get(clean)
        if clean_step:
            run_entire_step(clean_step, skip_env)


if __name__ == '__main__':
    main()
