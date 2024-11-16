# learn.scool.town
Platform: [OpenEdX](https://github.com/openedx/edx-platform) with the AGPL-3.0 license.

Framework: [Tutor](https://docs.tutor.edly.io/index.html) - the Docker-based Open edX distribution designed for peace of mind

## Development
Start dev: 
https://docs.tutor.edly.io/dev.html

Install `tutor`
```
pip install "tutor[full]"
```

Clone distributed git: `git@github.com:openedx/edx-platform.git`
```
git clone git@github.com:openedx/edx-platform.git

```

Then, optionally, tell Tutor to use a local fork of edx-platform:
```
tutor mounts add ./edx-platform
```

Then, launch the developer platform setup process:
```
tutor images build openedx-dev
tutor dev launch
```

Stopping the platform
To bring down the platform’s containers, simply run:
```
tutor dev stop
```