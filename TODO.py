- Create as little number of dependencies as possible.
- Have an agent run in the background that manages all build containers including listening on logs and errors
- Output a static file with status of all app build runs (in /tmp)

- When we build for distribution, we'll build the module to pull local tagged version.
- Run app stages in a container
  - start stages with multi-stage Dockerfile
  - add docker run instance in the job app index (app, process, etc)
  - capture output in seperate process
    - when the process is complete, inspect config and run any dependent stages or app jobs


- Test Cases
  - Multiple Apps
    - Parallel
      - Run apps in parallel in docker image builds
        - capture each containers id and index that with the app config to capture that app's dependencies
        - tail and watch logs and container status for errors, in the case of an error, propogate it and kill other parallel jobs (perform cleanup stage, if any exists) container builds unless the root config says otherwise
      - a. app -> build multi-stage dockerfile -> run docker container -> capture id -> put on queue
      - b. recieve app job id (celery) -> begin capturing logs, output -> handle success, errors
      - c.1. recieve error @ root -> lookup other parallel apps -> stop current app builds -> run cleanup stages for each or cleanup for root
      - c.2. recieve success @ root -> lookup that apps dependencies and spin those up, repeating step (a)
      - d. all app jobs done -> generate static site to view results -> report as complete
    - Sequential
      - Run each app as you would run a single app, based on the apps config is laid out
        - capture each containers id and index that with the app config to capture that app's dependencies
        - tail and watch logs and container status for errors, in the case of an error, propogate it to perform cleanup stage on any apps that specify it in their config
  - Single App
    - Parallel Stages
    - Sequential States
