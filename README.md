[![Build Status](https://travis-ci.com/smartgic/mycroft-sonos-controller-skill.svg?branch=20.8.1)](https://travis-ci.com/github/smartgic/mycroft-sonos-controller-skill) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-pink.svg?style=flat)](https://github.com/smartgic/mycroft-sonos-controller-skill/pulls) [![Skill: MIT](https://img.shields.io/badge/mycroft.ai-skill-blue)](https://mycroft.ai) [![Discord](https://img.shields.io/discord/809074036733902888)](https://discord.gg/Vu7Wmd9j)


# <img src="docs/sonos.png" card_color="#0000" style="vertical-align:bottom"/> Sonos Controller

Control Sonos speakers with music services support such as Spotify

## About

[Sonos](https://www.sonos.com) is the ultimate wireless home sound system: a whole-house WiFi network that fills your home with brilliant sound, room by room.

This skill interacts with your Sonos devices and allows you to play music from different music sources such as:
* Local library
* Spotify *(account required)*

Before using a music service, **make sure that you linked** your service account to your Sonos devices by using the Sonos application:

<img src='docs/sonos-app.png' width='450'/>

## Examples

* "play i got a feeling on living room"
* "play i got a feeling by black eyed peas on living room"
* "play i got a feeling from spotify on living room"
* "play i got a feeling by black eyed peas from spotify on living room"
* "play soundtrack playlist on dining room"
* "play soundtrack playlist from spotify on dining room"
* "play soundtrack album on dining room"
* "play soundtrack album from spotify on dining room"
* "discover sonos devices"
* "what is playing"
* "what are my music services"
* "much louder"
* "much quieter"
* "volume down"
* "volume up"
* "quieter"
* "louder"
* "pause music"
* "stop music"
* "resume music"
* "shuffle off"
* "shuffle on"
* "repeat off"
* "repeat on"
* "next music"
* "previous music"

## Installation

Make sure to be within the Mycroft `virtualenv` before running the `msm` command.

```
$ . mycroft-core/venv-activate.sh
$ msm install https://github.com/smartgic/mycroft-sonos-controller-skill.git
```

## Configuration

This skill utilizes the `settings.json` file which allows you to configure this skill via `home.mycroft.ai` after a few seconds of having the skill installed you should see something like below in the https://home.mycroft.ai/#/skill location:

<img src='docs/sonos-controller-config.png' width='450'/>

Fill this out with your appropriate information and hit the `save` button.

When Spotify music service is selected Mycroft will speak to you with a URL and code to follow. This URL is https://sonos.smartgic.io/CODE where `CODE` will be automatically and randomly generated by Mycroft and spoken to you *(e.g. Visit sonos.smartgic.io/QAZT2E)*.

This link will redirect you to the Sonos/Spotify authentication login page using `https` protocol.

<img src='docs/spotify-auth.png' width='450'/>

Once you successfully logged to Spotify, enter the same code as provided before into the `Link Code` field. Mycroft will confirm the configuration and gives you some example of what you could say.

## Credits

- Smart'Gic
- SoCo

## Category

**Music & Audio**

## Tags

#music
#audio
#sonos
#sound
#smarthome
#spotify