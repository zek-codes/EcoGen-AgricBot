import requests

k = {'latitude': 35.6875, 
    'longitude': 51.375,
    'generationtime_ms': 79.1100263595581,
    'utc_offset_seconds': 0,
    'timezone': 'GMT',
    'timezone_abbreviation': 'GMT',
    'elevation': 1173.0,
    'hourly_units': {
        'time': 'iso8601',
        'temperature_2m': '°C',
        'relativehumidity_2m': '%',
        'apparent_temperature': '°C',
        'precipitation': 'mm',
        'rain': 'mm',
        'windspeed_180m': 'km/h',
        'winddirection_180m': '°',
        'soil_temperature_0cm': '°C',
        'soil_moisture_0_1cm': 'm³/m³'
        },
    'hourly': {
        'time': [
            '2023-09-02T00:00', '2023-09-02T01:00', '2023-09-02T02:00',
            '2023-09-02T03:00', '2023-09-02T04:00', '2023-09-02T05:00',
            '2023-09-02T06:00', '2023-09-02T07:00', '2023-09-02T08:00',
            '2023-09-02T09:00', '2023-09-02T10:00', '2023-09-02T11:00',
            '2023-09-02T12:00', '2023-09-02T13:00', '2023-09-02T14:00',
            '2023-09-02T15:00', '2023-09-02T16:00', '2023-09-02T17:00',
            '2023-09-02T18:00', '2023-09-02T19:00', '2023-09-02T20:00',
            '2023-09-02T21:00', '2023-09-02T22:00', '2023-09-02T23:00',
            '2023-09-03T00:00', '2023-09-03T01:00', '2023-09-03T02:00',
            '2023-09-03T03:00', '2023-09-03T04:00', '2023-09-03T05:00',
            '2023-09-03T06:00', '2023-09-03T07:00', '2023-09-03T08:00',
            '2023-09-03T09:00', '2023-09-03T10:00', '2023-09-03T11:00',
            '2023-09-03T12:00', '2023-09-03T13:00', '2023-09-03T14:00',
            '2023-09-03T15:00', '2023-09-03T16:00', '2023-09-03T17:00',
            '2023-09-03T18:00', '2023-09-03T19:00', '2023-09-03T20:00',
            '2023-09-03T21:00', '2023-09-03T22:00', '2023-09-03T23:00',
            '2023-09-04T00:00', '2023-09-04T01:00', '2023-09-04T02:00',
            '2023-09-04T03:00', '2023-09-04T04:00', '2023-09-04T05:00',
            '2023-09-04T06:00', '2023-09-04T07:00', '2023-09-04T08:00', '2023-09-04T09:00', '2023-09-04T10:00', '2023-09-04T11:00', '2023-09-04T12:00', '2023-09-04T13:00', '2023-09-04T14:00', '2023-09-04T15:00', '2023-09-04T16:00', '2023-09-04T17:00', '2023-09-04T18:00', '2023-09-04T19:00', '2023-09-04T20:00', '2023-09-04T21:00', '2023-09-04T22:00', '2023-09-04T23:00', '2023-09-05T00:00', '2023-09-05T01:00', '2023-09-05T02:00', '2023-09-05T03:00', '2023-09-05T04:00', '2023-09-05T05:00', '2023-09-05T06:00', '2023-09-05T07:00', '2023-09-05T08:00', '2023-09-05T09:00', '2023-09-05T10:00', '2023-09-05T11:00', '2023-09-05T12:00', '2023-09-05T13:00', '2023-09-05T14:00', '2023-09-05T15:00', '2023-09-05T16:00', '2023-09-05T17:00', '2023-09-05T18:00', '2023-09-05T19:00', '2023-09-05T20:00', '2023-09-05T21:00', '2023-09-05T22:00', '2023-09-05T23:00', '2023-09-06T00:00', '2023-09-06T01:00', '2023-09-06T02:00', '2023-09-06T03:00', '2023-09-06T04:00', '2023-09-06T05:00', '2023-09-06T06:00', '2023-09-06T07:00', '2023-09-06T08:00', '2023-09-06T09:00', '2023-09-06T10:00', '2023-09-06T11:00', '2023-09-06T12:00', '2023-09-06T13:00', '2023-09-06T14:00', '2023-09-06T15:00', '2023-09-06T16:00', '2023-09-06T17:00', '2023-09-06T18:00', '2023-09-06T19:00', '2023-09-06T20:00', '2023-09-06T21:00', '2023-09-06T22:00', '2023-09-06T23:00', '2023-09-07T00:00', '2023-09-07T01:00', '2023-09-07T02:00', '2023-09-07T03:00', '2023-09-07T04:00', '2023-09-07T05:00', '2023-09-07T06:00', '2023-09-07T07:00', '2023-09-07T08:00', '2023-09-07T09:00', '2023-09-07T10:00', '2023-09-07T11:00', '2023-09-07T12:00', '2023-09-07T13:00', '2023-09-07T14:00', '2023-09-07T15:00', '2023-09-07T16:00', '2023-09-07T17:00', '2023-09-07T18:00', '2023-09-07T19:00', '2023-09-07T20:00', '2023-09-07T21:00', '2023-09-07T22:00', '2023-09-07T23:00', '2023-09-08T00:00', '2023-09-08T01:00', '2023-09-08T02:00', '2023-09-08T03:00', '2023-09-08T04:00', '2023-09-08T05:00', '2023-09-08T06:00', '2023-09-08T07:00', '2023-09-08T08:00', '2023-09-08T09:00', '2023-09-08T10:00', '2023-09-08T11:00', '2023-09-08T12:00', '2023-09-08T13:00', '2023-09-08T14:00', '2023-09-08T15:00', '2023-09-08T16:00', '2023-09-08T17:00', '2023-09-08T18:00', '2023-09-08T19:00', '2023-09-08T20:00', '2023-09-08T21:00', '2023-09-08T22:00', '2023-09-08T23:00'
            ],
        'temperature_2m': [
            23.7, 23.3, 22.1,
            22.7, 26.2, 29.8,
            31.4, 32.6, 33.6,
            34.5, 35.2, 35.6,
            35.6, 35.2, 34.4,
            32.7, 30.8, 27.7, 26.9, 26.5, 26.3, 26.0, 26.1, 26.2, 25.2, 25.5, 23.6, 24.4, 26.2, 29.4, 31.4, 32.3, 33.5, 34.5, 35.1, 35.6, 35.7, 35.3, 34.5, 32.5, 30.7, 28.5, 27.5, 27.3, 27.6, 26.7, 25.7, 24.9, 25.0, 25.1, 24.7, 24.6, 27.4, 30.6, 32.2, 33.5, 34.7, 35.6, 36.3, 36.5, 36.3, 35.9, 35.1, 33.1, 31.5, 28.4, 27.2, 27.8, 27.4, 26.9, 26.5, 26.2, 25.6, 25.2, 24.9, 25.0, 27.7, 31.3, 33.8, 35.2, 36.1, 36.9, 37.6, 38.1, 38.0, 37.3, 36.0, 34.5, 32.7, 30.7, 28.9, 27.7, 26.8, 25.9, 25.1, 24.3, 23.7, 22.9, 22.2, 22.8, 25.7, 29.7, 33.0, 34.6, 35.4, 36.0, 36.7, 37.3, 37.3, 36.5, 35.2, 33.7, 32.0, 30.1, 28.5, 27.3, 26.5, 25.9, 25.8, 25.9, 25.8, 25.0, 23.9, 24.1, 26.6, 30.2, 32.9, 32.7, 33.6, 34.3, 34.8, 35.0, 34.8, 34.0, 32.8, 31.5, 30.1, 28.5, 27.3, 26.8, 26.8, 26.7, 26.6, 26.5, 26.4, 26.3, 26.1, 26.7, 28.4, 30.7, 32.7, 34.0, 35.0, 35.7, 36.0, 36.1, 36.2, 35.8, 35.8, 35.4, 34.5, 33.3, 32.2, 31.6, 31.2, 30.7, 30.0, 29.3
            ],
        'relativehumidity_2m': [
            30, 33, 34,
            37, 32, 24,
            21, 19, 17,
            16, 15, 14,
            14, 14, 14,
            17, 19, 24, 24, 23, 26, 28, 27, 27, 29, 32, 33, 32, 33, 26, 21, 19, 17, 16, 14, 13, 12, 13, 13, 16, 19, 22, 22, 22, 22, 24, 25, 27, 26, 25, 26, 27, 27, 20, 17, 13, 12, 12, 11, 11, 11, 12, 12, 14, 16, 21, 22, 20, 21, 22, 23, 23, 24, 24, 25, 26, 26, 22, 16, 13, 12, 11, 11, 10, 10, 10, 10, 11, 12, 13, 15, 19, 23, 26, 25, 23, 21, 21, 21, 21, 19, 15, 13, 13, 14, 14, 13, 11, 10, 9, 9, 10, 13, 18, 21, 22, 21, 21, 21, 22, 23, 26, 30, 31, 27, 21, 16, 16, 14, 13, 13, 13, 14, 15, 16, 17, 18, 20, 21, 22, 22, 22, 22, 21, 21, 21, 21, 21, 19, 16, 14, 13, 12, 12, 12, 11, 11, 10, 10, 12, 15, 18, 21, 22, 22, 23, 24, 26
            ],
        'apparent_temperature': [
            21.8, 22.0,
            20.0, 21.2,
            25.3, 28.6,
            29.7, 31.1,
            32.4, 33.5,
            34.1, 33.9, 33.1, 32.4, 31.9, 31.0, 29.0, 25.6, 24.7, 24.1, 24.2, 24.1, 24.0, 24.3, 23.6, 24.2, 21.9, 22.9, 25.4, 28.4, 29.8, 29.9, 31.8, 33.2, 33.4, 33.5, 32.9, 32.3, 31.5, 30.3, 28.8, 26.2, 25.2, 24.7, 25.4, 24.6, 23.4, 22.6, 22.5, 22.6, 22.3, 22.5, 26.1, 28.7, 29.7, 31.2, 32.4, 33.9, 34.4, 33.9, 33.1, 32.7, 31.7, 30.6, 29.3, 26.0, 24.6, 25.1, 24.8, 24.4, 24.1, 23.7, 23.2, 22.7, 22.4, 22.8, 26.3, 30.3, 31.9, 33.4, 34.7, 35.5, 36.4, 36.4, 35.3, 34.3, 32.9, 31.4, 29.6, 27.6, 25.9, 25.1, 24.7, 24.1, 22.9, 21.7, 20.7, 19.7, 19.0, 19.8, 23.2, 27.4, 30.3, 32.6, 33.9, 34.6, 35.1, 34.8, 33.8, 32.5, 31.4, 30.4, 29.6, 28.0, 26.1, 24.7, 23.7, 23.1, 22.9, 23.2, 23.3, 22.7, 21.9, 22.3, 25.1, 29.1, 31.1, 30.4, 31.2, 31.6, 32.0, 31.9, 31.3, 30.6, 29.8, 28.8, 27.6, 26.1, 24.6, 23.9, 23.8, 23.7, 23.5, 23.3, 23.2, 23.0, 22.7, 23.4, 25.2, 27.2, 28.7, 30.7, 31.9, 32.8, 33.0, 32.7, 32.1, 32.1, 30.9, 30.4, 30.7, 31.1, 30.9, 29.9, 29.1, 28.6, 27.9, 27.3
            ],
        'precipitation': [
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
            ],
        'rain': [
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
            ],
        'windspeed_180m': [
            15.8, 8.8, 4.6,
            1.8, 5.9, 2.6,
            8.4, 13.7, 14.3,
            13.8, 12.9, 11.9,
            12.1, 10.3, 8.1,
            7.0, 7.1, 8.8,
            10.0, 16.3, 18.6,
            19.1, 21.1, 20.1,
            14.3, 15.9, 4.0, 10.1, 4.8, 4.9, 5.1, 9.7, 13.3, 14.6, 13.7, 12.8, 12.1, 12.4, 13.2, 16.4, 19.6, 15.1, 12.0, 10.8, 11.0, 10.1, 10.8, 10.5, 14.6, 16.0, 15.6, 11.5, 9.6, 7.4, 11.2, 11.8, 16.3, 14.2, 13.4, 14.5, 12.5, 11.8, 17.7, 19.6, 13.6, 10.8, 11.9, 15.6, 18.2, 19.1, 18.1, 18.4, 16.3, 15.8, 14.8, 11.7, 10.9, 4.5, 5.7, 9.8, 11.4, 11.5, 10.0, 7.3, 9.0, 10.9, 18.7, 23.3, 20.1, 17.6, 18.7, 16.2, 10.4, 6.2, 5.9, 7.2, 7.4, 6.2, 5.1, 5.5, 5.7, 5.6, 6.2, 8.9, 13.0, 15.5, 15.7, 16.8, 18.3, 20.6, 22.6, 19.9, 9.1, 11.6, 22.4, 23.8, 20.2, 17.3, 17.3, 17.9, 17.1, 13.5, 8.8, 6.0, 4.6, 2.9, 2.2, 11.1, 16.0, 19.5, 20.2, 19.5, 18.4, 18.0, 18.5, 19.4, 18.7, 17.2, 15.8, 14.1, 12.5, 12.4, 13.7, 15.3, 16.4, 17.5, 18.0, 17.9, 17.2, 18.4, 20.2, 21.0, 21.9, 23.1, 23.2, 22.1, 21.1, None, None, None, None, None, None, None, None, None, None, None
            ],
        'winddirection_180m': [
            45, 102, 135,
            360, 346, 286,
            220, 203, 205,
            208, 207, 209,
            207, 209, 212, 201, 156, 109, 60, 49, 44, 49, 46, 46, 118, 167, 355, 358, 27, 54, 172, 184, 178, 171, 166, 164, 153, 154, 154, 151, 144, 108, 97, 53, 49, 90, 105, 96, 80, 67, 52, 58, 77, 133, 184, 168, 166, 156, 149, 174, 168, 149, 142, 137, 148, 120, 65, 40, 38, 36, 41, 42, 45, 45, 41, 43, 63, 76, 198, 204, 193, 194, 195, 213, 217, 264, 293, 305, 324, 359, 25, 32, 34, 36, 38, 37, 39, 54, 86, 113, 125, 130, 144, 159, 166, 175, 191, 211, 227, 237, 245, 253, 279, 30, 46, 51, 55, 59, 59, 56, 55, 61, 78, 107, 129, 150, 180, 193, 188, 185, 185, 185, 181, 168, 151, 138, 128, 119, 107, 94, 78, 64, 60, 60, 61, 58, 53, 56, 70, 91, 109, 125, 139, 149, 152, 152, 150, None, None, None, None, None, None, None, None, None, None, None
            ],
        'soil_temperature_0cm': [
            20.6, 19.5, 20.1,
            22.0, 28.7, 36.0,
            40.1, 42.2, 44.1,
            45.5, 45.2, 44.2,
            41.8, 38.2, 33.9, 28.7, 25.8, 25.1, 24.6, 24.0, 23.8, 23.6, 23.9, 23.5, 22.3, 21.5, 22.0, 23.3, 27.0, 34.3, 37.5, 40.0, 43.1, 44.7, 44.4, 44.1, 41.7, 37.8, 33.6, 29.1, 27.0, 26.2, 25.4, 25.8, 25.2, 24.2, 23.5, 22.9, 23.0, 22.7, 22.0, 23.2, 29.3, 36.5, 39.8, 42.6, 44.5, 46.3, 46.4, 44.4, 41.9, 38.5, 34.2, 29.4, 26.7, 26.0, 25.2, 25.3, 24.5, 23.9, 23.4, 23.3, 22.7, 22.5, 21.8, 23.1, 29.0, 36.7, 42.4, 45.2, 47.0, 47.9, 48.3, 47.7, 44.8, 40.5, 35.0, 30.6, 28.1, 26.7, 25.5, 24.4, 23.6, 22.9, 22.1, 21.4, 20.9, 20.2, 19.7, 21.4, 27.2, 35.2, 41.5, 44.5, 45.8, 46.1, 45.7, 44.3, 42.0, 38.2, 33.4, 29.6, 27.5, 26.4, 25.5, 24.5, 23.8, 23.3, 23.0, 22.9, 22.9, 22.2, 21.5, 22.8, 27.9, 35.0, 40.2, 43.4, 45.7, 46.7, 46.2, 44.4, 41.8, 37.7, 32.7, 28.8, 26.7, 25.6, 24.8, 24.2, 23.9, 23.6, 23.3, 23.1, 23.0, 22.8, 22.7, 24.3, 29.1, 35.5, 40.9, 44.4, 46.7, 47.8, 46.8, 44.5, 42.8, None, None, None, None, None, None, None, None, None, None, None
            ],
        'soil_moisture_0_1cm': [
            0.081, 0.083, 0.084,
            0.083, 0.084, 0.083,
            0.081, 0.079, 0.076,
            0.074, 0.072, 0.07,
            0.069, 0.069, 0.069, 0.07, 0.071, 0.072, 0.073, 0.074, 0.075, 0.075, 0.076, 0.077, 0.078, 0.079, 0.08, 0.081, 0.081, 0.081, 0.08, 0.078, 0.076, 0.074, 0.072, 0.07, 0.069, 0.069, 0.069, 0.07, 0.07, 0.071, 0.072, 0.073, 0.074, 0.074, 0.075, 0.076, 0.077, 0.077, 0.078, 0.079, 0.079, 0.079, 0.077, 0.075, 0.073, 0.071, 0.07, 0.068, 0.068, 0.068, 0.068, 0.068, 0.07, 0.071, 0.072, 0.072, 0.073, 0.074, 0.075, 0.075, 0.076, 0.077, 0.077, 0.078, 0.078, 0.078, 0.076, 0.074, 0.072, 0.07, 0.068, 0.067, 0.067, 0.067, 0.067, 0.067, 0.068, 0.069, 0.07, 0.071, 0.071, 0.072, 0.073, 0.074, 0.075, 0.076, 0.077, 0.077, 0.077, 0.077, 0.076, 0.074, 0.072, 0.07, 0.069, 0.068, 0.067, 0.067, 0.067, 0.068, 0.069, 0.069, 0.07, 0.071, 0.072, 0.073, 0.074, 0.074, 0.075, 0.075, 0.076, 0.076, 0.076, 0.075, 0.075, 0.075, 0.073, 0.072, 0.071, 0.071, 0.071, 0.071, 0.072, 0.072, 0.073, 0.073, 0.074, 0.075, 0.075, 0.076, 0.076, 0.077, 0.077, 0.077, 0.078, 0.078, 0.077, 0.076, 0.075, 0.074, 0.072, 0.071, 0.07, 0.07, 0.07, None, None, None, None, None, None, None, None, None, None, None
            ]
        }
    }

def wether_forecast(latitude, longitude):
    url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,rain,windspeed_180m,winddirection_180m,soil_temperature_0cm,soil_moisture_0_1cm'.format(latitude, longitude)
    response = requests.get(url)
    weather = response.json()
    return weather


def from_json_to_readalble_forecast(weather):
    text = """"""
    for x in range(len(weather['hourly']['time'])):
        text += f"""In {weather['hourly']['time'][x]} the temperature will be {weather['hourly']['temperature_2m'][x]} and the humidity will be {weather['hourly']['relativehumidity_2m'][x]} and the wind speed will be {weather['hourly']['windspeed_180m'][x]} and the precipitation will be {weather['hourly']['precipitation'][x]} and the rain will be {weather['hourly']['rain'][x]} and the soil temperature will be {weather['hourly']['soil_temperature_0cm'][x]} and the soil moisture will be {weather['hourly']['soil_moisture_0_1cm'][x]} \n\n"""
    return text

print(from_json_to_readalble_forecast(wether_forecast(35.6897, 51.3890)))


def from_json_to_text(weather):
    text = f'''
Temperature (°C or °F): {weather['hourly']['temperature_2m'][0]}

Humidity Percentage (%): {weather['hourly']['relativehumidity_2m'][0]}%

Wind Speed (mph or km/h): {weather['hourly']['windspeed_180m'][0]}

Precipitation (mm or inches): {weather['hourly']['precipitation'][0]}

Rain (hours of daylight): {weather['hourly']['rain'][0]}

Soil temperature 0cm: {weather['hourly']['soil_temperature_0cm'][0]}

Agricultural Information: {weather['hourly']['soil_temperature_0cm'][0]}

Types of Available Grasses: 

Soil Quality: 

Nutritional Requirements of the Animals: 

Weather Forecasts: 

'''
    return text