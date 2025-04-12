class PlexPersonalMovieAgent(Agent.Movies):
    name = 'Personal Movies'
    languages = [Locale.Language.NoLanguage]
    contributes_to = ['com.plexapp.agents.localmedia', 'com.plexapp.agents.none']

    def search(self, results, media, lang):
        results.Append(MetadataSearchResult(id=media.id, name=media.name, year=media.year, lang=lang, score=100))

    def update(self, metadata, media, lang, force=False):
        return metadata
