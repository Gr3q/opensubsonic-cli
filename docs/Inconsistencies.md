# Inconsistencies/Issues

* `ItemDate` description and spec doesn't match (in required fields)
* Disc number must be a number but obviously it can be other things
* `getAlbumInfo2` return type incorrect (based on `AlbumList`)?
* `downloadPodcastEpisode` return type incorrect?
* `deleteBookmark` summary and description is wrong
* `download` error payload schema missing completely
* `getArtists` page first `artists` link is broken
* `getAvatar` `username` parameter is "required" and has a "default" as well. it should be one or the other
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
* Typo in `search` `album` parameters's comment
* `search` `any` parameter type unclear
* `SearchResult` is not documented
* `SearchResult2` all field details are incorrect
* `stream` `timeOffset` param's description typo, "Transcode Offet"
* [tokenInfo](https://opensubsonic.netlify.app/docs/responses/tokeninfo/) data is too deeply nested in docs?
* [tokenInfo](https://opensubsonic.netlify.app/docs/endpoints/tokeninfo/) says "A subsonic-response element with a nested tokenInfo on success, or error 44 on invalid token.". Does that mean it cannot return any other error code on error?
* `unstar` summary is incorrect
* `updateuser` is missing `playlistRole` parameter?
* `createuser` is missing `maxBitRate` parameter?

## Future Improvements

* Could use inheritance for ArtistInfo and ArtistInfo2
* `getPodcasts` payload dependent on query param `includeEpisodes`, but it doesn't indicate that structurally.
* `jukeboxControl` payload dependent on query param `action: get`, but it doesn't indicate that structurally.
* `getAlbumList` and `getAlbumList2` POST params can be a tagged union
* `jukeboxcontrol` POST params can be a tagged union
* Add version info for each endpoint and add 404 responses where the endpoint didn't exist since v1

## Differences from spec

* Some typo fixes I failed to document:(
* Added minimum: 0 to integer types where it's implied (`count`, `offset`, unix timestamp, `position`)
* forces json format on every endpoint
* All extensions are added to the schema and tagged as "Extension", and have a 404 return type as well that described as "Not Implemented"
* Excluded `example`s, opted to use `externalDocs` only because it made the Swagger and Redoc generated documents harder to read. I might add them if they make sense for generated client code.
* Extension query parameters are denoted, but nothing else can be done about them.
* `HTTP form POST` extension support might be stricter than what's allowed (global params only allowed as query params, endpoint specific params are the ones allowed in request body)
