# Home Assistant Integration - ekey (legacy)

Home Assistant integration for ekey home or multi (legacy)

[![Static Badge](https://img.shields.io/badge/HACS-Custom-41BDF5?style=for-the-badge&logo=homeassistantcommunitystore&logoColor=white)](https://github.com/hacs/integration) 
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/klein0r/ha-ekeylegacy/total?style=for-the-badge)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/klein0r/ha-ekeylegacy?style=for-the-badge)

![GitHub Release Date](https://img.shields.io/github/release-date-pre/klein0r/ha-ekeylegacy?style=for-the-badge&label=Latest%20Beta%20Release) [![GitHub Release](https://img.shields.io/github/v/release/klein0r/ha-ekeylegacy?include_prereleases&style=for-the-badge)](https://github.com/klein0r/ha-ekeylegacy/releases)

![GitHub Release Date](https://img.shields.io/github/release-date/klein0r/ha-ekeylegacy?style=for-the-badge&label=Latest%20Release) [![GitHub Release](https://img.shields.io/github/v/release/klein0r/ha-ekeylegacy?style=for-the-badge)](https://github.com/klein0r/ha-ekeylegacy/releases)

## Setup

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=klein0r&repository=ha-ekeylegacy&category=Integration)

## Event data

The integration listens for UDP packets sent by the ekey LAN adapter and triggers an `authenticated` or `failed` event. The packet format depends on the configured protocol.

### ekey home

Example packet: `1_0046_4_80156809150025_1_2`

| Attribute | Example          | Description                                        |
|-----------|------------------|----------------------------------------------------|
| `type`    | `1`              | Packet type                                        |
| `user`    | `46`             | User ID (leading zeros removed)                    |
| `finger`  | `4`              | Finger ID (`R` if an RFID tag was used)            |
| `scanner` | `80156809150025` | Serial number of the finger scanner                |
| `action`  | `1`              | Action (`1` = access granted, `2` = access denied) |
| `relay`   | `2`              | Switched relay                                     |

### ekey multi

Example packet: `1_00003_-----JOSEF_1_7_2_80156809150025_-GAR_1_-`

| Attribute       | Example          | Description                                        |
|-----------------|------------------|----------------------------------------------------|
| `type`          | `1`              | Packet type                                        |
| `user`          | `3`              | User ID (leading zeros removed)                    |
| `user_name`     | `JOSEF`          | User name (leading dashes removed)                 |
| `user_status`   | `1`              | User status                                        |
| `finger`        | `7`              | Finger ID (`R` if an RFID tag was used)            |
| `key`           | `2`              | Key ID                                             |
| `scanner`       | `80156809150025` | Serial number of the finger scanner                |
| `scanner_name`  | `GAR`            | Scanner name (leading dashes removed)              |
| `action`        | `1`              | Action (`1` = access granted, `2` = access denied) |
| `digital_input` | `-`              | Digital input ID                                   |

Unlike the home protocol, the multi protocol does not transmit the switched relay. Instead, the key ID is transmitted.

## License

The MIT License (MIT)

Copyright (c) 2026 Matthias Kleine <info@haus-automatisierung.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
