Roost [WIP]
=====
The best cli deploy tool for mono-repos.

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
