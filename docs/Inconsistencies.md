# Inconsistencies

* `ItemDate` description and spec doesn't match (in required fields)
* Disc number must be a number but obviously it can be other things
* `getAlbumInfo2` return type incorrect (based on `AlbumList`)?
* `downloadPodcastEpisode` return type incorrect?
* `deleteBookmark` summary and description is wrong
* `download` error payload schema missing completely
* `getArtists` page first `artists` link is broken
* `getAvatar` `username` parameter is "required" and has a "default" as well.
* `getCaptions` return payload not clear
* `getCoverArt` `size` param type not specified, I assume `int` as pixels
* `Indexes` `ignoredArticles` pattern is unclear, it was comma-separated list as string before
* `internetRadioStation` `homePageUrl` has wrong details
* `getLyrics` `artist` and `title` query parameters are really optional?
* is `getLyrics` returns only one element?

## Future Improvements

* Could use inheritance for ArtistInfo and ArtistInfo2
