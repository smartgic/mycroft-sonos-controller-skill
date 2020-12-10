from mycroft import MycroftSkill, intent_handler
from soco import discover
from soco.music_services import MusicService
from soco.discovery import by_name
from soco import exceptions
from random import choice


class SonosController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.speakers = []
        self.services = []
        self.service = 'Spotify'
        self.provider = MusicService(self.service)

    def _discovery(self):
        try:
            self.speakers = discover()
        except exceptions.SoCoException as e:
            self.log.error(e)

        if not self.speakers:
            self.log.warning(
                'I could not find any devices on your network')
            self.speak_dialog('error.disovery')
        else:
            self.log.info(
                '{} device(s) found'.format(len(self.speakers)))

    def _subscribed_services(self):
        try:
            # Commented until SoCo integrates this method back
            # self.services = MusicService.get_subscribed_services_names()
            self.services = ['Spotify', 'Amazon Music']
            return self.services
        except exceptions.SoCoException as e:
            self.log.error(e)

    def _check_category(self, category):
        for categories in self.provider.available_search_categories:
            if category in categories:
                return True
        return False

    def _check_speaker(self, speaker):
        for device in self.speakers:
            if speaker in device.player_name.lower():
                self.log.info('{} speaker found'.format(speaker))
                return device.player_name
        return False

    @intent_handler('sonos.discovery.intent')
    def handle_speaker_discovery(self, message):
        self._discovery()
        if self.speakers:
            self.speak_dialog('sonos.discovery', data={
                              "total": len(self.speakers)})
            list_device = self.ask_yesno('sonos.list')
            if list_device == 'yes':
                for speaker in self.speakers:
                    self.speak(speaker.player_name.lower())

    @intent_handler('sonos.service.intent')
    def handle_subscribed_services(self, message):
        if self.services:
            self.speak_dialog('sonos.service', data={
                              "total": len(self.services)})
            list_service = self.ask_yesno('sonos.list')
            if list_service == 'yes':
                for service in self.services:
                    self.speak(service)
            return self.services
        else:
            self.log.warning('no subscription found for any music service')
            self.speak_dialog('error.list')

    @intent_handler('sonos.playlist.intent')
    def handle_playlist(self, message):
        service = self.service
        if message.data.get('service'):
            service = message.data.get('service')
        playlist = message.data.get('playlist')
        speaker = message.data.get('speaker')

        if self.services and service in self.services:
            device_name = self._check_speaker(speaker)
            if device_name:
                if self._check_category('playlists'):
                    try:
                        playlists = self.provider.search('playlists', playlist)
                        device = by_name(device_name)
                        self.log.info('device selected {}'.format(device))
                        device.clear_queue()
                        device.add_to_queue(choice(playlists))
                        device.play()
                    except exceptions.SoCoException as e:
                        self.log.error(e)
                else:
                    self.log.warning(
                        'there is no playlist category for this service')
                    self.speak_dialog('error.category', data={
                        "category": playlist})
            else:
                self.log.warning(
                    '{} speaker not found'.format(speaker))
                self.speak_dialog('error.speaker', data={
                    "speaker": speaker})

    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()
        self._discovery()
        self._subscribed_services()

    def on_settings_changed(self):
        return


def create_skill():
    return SonosController()
