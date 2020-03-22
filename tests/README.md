# Test Strategy

apiKey value testing is currently being ommitted as API authentication should be ideally tested separately. All APIs should share authentication logic, testing in combination with query fields yields unnecessarily complex test result data.

## City Name
```
https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}
```

### Simple happy paths

Use the same city to limit variables, otherwise, data outages might affect results.

1. Regularly capitalized single word city
   1. London \[expect: 200]
2. uppercase single word city name
   1. LONDON \[expect: 200]
3. lowercase single word city name
   1. london \[expect: 200]

### Numbers
1. Arabic numerals
   1. 29 Palms \[expect: 404]
2. Written numbers
   1. Twentynine palms \[expect: 200]

### Special characters

Some common cases that might occur. Again, use the same city name where appropriate to limit variables.

1. Dash(es) in city name
   1. Milton-Freewater \[expect: 200]
   2. Stratford-upon-Avon \[expect: 200]
2. Space(s) in city name
   1. New York \[expect: 200]
   2. Ho Chi Minh City \[expect: 200]
3. Leading spaces
   1. 1 space before 'New York' \[expect: 200]
   2. 2 spaces before 'New York' \[expect: 200]
4. Trailing spaces
   1. 1 space after 'New York' \[expect: 200]
   2. 2 spaces after 'New York' \[expect: 200]
5. Quoted city name
   1. single quoted 'New York' \[expect: 404]
   2. double quoted "New York" \[expect: 404]
   
### Non-existent city
1. Imaginary city
   1. Shambala \[expect: 404]

## Zip Code
```
https://api.openweathermap.org/data/2.5/weather?zip={zipCode},{countryCode}&appid={apiKey}
```
### Happy path

Use the same zip code to limit variability.

1. Valid US zip code with lowercase country code
   1. 94040,us \[expect: 200]
1. Valid US zip code only
   1. 94040 \[expect: 200]
1. Valid US zip code with uppercase country code
   1. 94040,US \[expect: 200]
1. Valid US zip code with CamelCase country code
   1. 94040,Us \[expect: 200]
1. Valid US zip code with invalid country code
   1. 94040,usa \[expect: 404]
   
### Failure paths

Use the same zip code to limit variability.

1. Invalid zip code with country code
   1. c4f3b4b3,us \[expect: 404]
2. Invalid zip code only
   1. c4f3b4b3 \[expect: 404]