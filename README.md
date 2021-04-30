Roost [WIP]
=====
The best cli deploy tool for mono-repos.

# Usage
Each app in the repo will have it's own config, this will allow the passing of the app path to the cli and all stage related commands can now be accessed.
## Example project usage
```
proj_root/
    client_app/
        ...misc files
        .roost.yaml
    server_app/
        ...misc files
        .roost.yaml
    other_app/
        ...misc files
        .roost.yaml
    ...misc files
    .roost.yaml
```
## Executing an app build, deploy, or other stage execution
This is a very basic example where within the proj_root directory from the example above, we can execute a "full" or `--full` execution of all stages configured in the client_app/.roost.yaml file.
```shell
$ roost --app client_app --full
```

You're also allowed to pass environment variables like so.
```shell
$ roost --app client_app --full --env MYENV=heyguys --env HI=oh hi
```

Or specify an individual stage or even multiple stages to execute.
```shell
$ # specify a single
$ roost --app client_app --build
$
$ # or several
$ roost --app client_app --build --deploy --clean
```

# How to structure the root project's YAML config [WIP]
This is a big work in progress, that said although this is optional, it would be safe to have for future versions.
```yaml
mode: root
groups:
  first_group:test:
    parallel: true
    apps:
      client_app:
        env:
          ENV: test
        stages:
          - build
          - deploy
      other_app:
        stages:
          - deploy
  second_group:test:
    parallel: false
    env:
      ENV: test
    apps:
      server_app:
      backup_app:
```
## What execution might look like
```shell
$ roost --group first_group:test
```

# How to structure each application's YAML config
```yaml
mode: app
pre_build:
  env:
    SOME_ENV: thevalue
  exec:
    - some command
  script:
    - some_script.sh
build:
  env:
    SOME_ENV: thevalue
  exec:
    - some command
  script:
    - some_script.sh
pre_deploy:
  env:
    SOME_ENV: thevalue
  exec:
    - some command
  script:
    - some_script.sh
deploy:
  env:
    SOME_ENV: thevalue
  exec:
    - some command
  script:
    - some_script.sh
clean:
  env:
    SOME_ENV: thevalue
  exec:
    - some command
  script:
    - some_script.sh
```

# Features TODO
Things I want to do or have done.
- [x] Basic stages working
- [ ] Project level config for multiple and custom deploy groups
- [ ] Parallel executions for app deploys
- [ ] More stages...some that come to mind could be `migrate` accompanied with `pre/post` and a `tag` stage.
- [ ] Custom stages, or at least creating alias to the built-in stages
- [ ] Potential `roost` stage that provides some special features but also may provide configuration for dependency chains
