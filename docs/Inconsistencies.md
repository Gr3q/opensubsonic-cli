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
* Extension not supported error is unclear, assumed servers will 404 on the request.
* `PodcastEpisode` description "PodcastEntry extends Child". Wrong name used?
* `NowPlayingEntry` `minutesAgo` format is unclear
* `PlayQueue` description incorrect
* `PodcastChannel` `errorMessage` existence could depend on `status` in documentation?
* `GetSimilarSongs` and `GetSimilarSongs2` response type is the same in the spec (not the names)?
* `User` example uses booleans and integers as strings, but they are typed as booleans and integers.
* `VideoInfo` is not documented
* `Videos` is not documented
* `hls` endpoint summary matches `download`

## Future Improvements

* Could use inheritance for ArtistInfo and ArtistInfo2
* `getPodcasts` payload dependent on query param `includeEpisodes`, could indicate that.
