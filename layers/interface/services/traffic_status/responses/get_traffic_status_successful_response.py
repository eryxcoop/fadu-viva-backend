class GetTrafficStatusSuccessfulResponse:
    def __init__(self, json_response):
        self._traffic_data = self._build_traffic_data_from_json_response(json_response)

    @staticmethod
    def _build_traffic_data_from_json_response(json_response):
        return json_response["RWS"][0]["RW"]

    def _get_main_street_data(self, main_street, way):
        # Filtered list contains one street_data for each way of the street
        return [street_data for street_data in self._traffic_data if street_data["DE"] == main_street][way]

    @staticmethod
    def _get_flow_in_crossing_streets(main_street_data, first_crossing_street, second_crossing_street):
        flow_items = main_street_data['FIS'][0]['FI']
        return [item for item in flow_items if item["TMC"]["DE"] in [first_crossing_street, second_crossing_street]]

    @staticmethod
    def _calculate_traffic_status(flow_in_crossing_streets):
        first_crossing_street_flow = flow_in_crossing_streets[0]
        second_crossing_street_flow = flow_in_crossing_streets[1]

        first_jam_factor = first_crossing_street_flow["CF"][0]["JF"]
        second_jam_factor = second_crossing_street_flow["CF"][0]["JF"]

        average_jam_factor_in_main_street = (first_jam_factor + second_jam_factor) / 2

        return average_jam_factor_in_main_street

    def get_status_for(self, main_street, first_crossing_street, second_crossing_street, way=0):
        """Returns a number between 0 and 10, which is the average jam factors between crossing streets.

            Parameters
            ----------
            main_street : str, required
                The name of the requested street.

            first_crossing_street : str, required
                The name of one crossing street to the main street.

            second_crossing_street : str, required
                The name of one crossing street to the main street. This street is assumed to be contiguous to
                first_crossing_street in the order of the driving direction.

            way : number [0, 1], optional
                The direction of the roadway (default is 0)
        """
        main_street_data = self._get_main_street_data(main_street, way)
        flow_in_crossing_streets = self._get_flow_in_crossing_streets(main_street_data, first_crossing_street,
                                                                      second_crossing_street)
        return self._calculate_traffic_status(flow_in_crossing_streets)

    @classmethod
    def _default_response(cls):
        """Prints an example HERE API response for a request of traffic on a specific street.

            A quick reference about the meaning of acronyms in this example response could be found in
            'https://developer.here.com/documentation/traffic/dev_guide/topics/common-acronyms.html'
        """
        return {
            'RWS': [{
                'RW': [
                    {
                        'FIS': [
                            {
                                'FI': [
                                    {
                                        'TMC': {
                                            'PC': 2264,
                                            'DE': 'Avenida Del Libertador',
                                            'QD': '-',
                                            'LE': 0.07821
                                        },
                                        'SHP': [],
                                        'CF': [
                                            {
                                                'TY': 'TR',
                                                'SP': 13.0,
                                                'SU': 13.0,
                                                'FF': 25.3,
                                                'JF': 3.67588,
                                                'CN': 0.7
                                            }
                                        ]
                                    },
                                    {
                                        'TMC': {
                                            'PC': 2265,
                                            'DE': 'Avenida Presidente Figueroa Alcorta',
                                            'QD': '-',
                                            'LE': 0.32501
                                        },
                                        'SHP': [],
                                        'CF': [
                                            {
                                                'TY': 'TR',
                                                'SP': 15.0,
                                                'SU': 15.0,
                                                'FF': 30.6,
                                                'JF': 2.9,
                                                'CN': 0.7
                                            }
                                        ]
                                    }
                                ]
                            }
                        ],
                        'mid': '420d330f-57f4-4d4f-94aa-db7c8db748a6',
                        'LI': 'A47+02263',
                        'DE': 'Avenida G Udaondo',
                        'PBT': '2020-03-18T21:13:41Z'
                    },
                    {
                        'FIS': [
                            {
                                'FI': [
                                    {
                                        'TMC': {
                                            'PC': 2267,
                                            'DE': 'Avenida Int Cantilo',
                                            'QD': '+', 'LE': 0.42206
                                        },
                                        'SHP': [],
                                        'CF': [{
                                            'TY': 'TR',
                                            'SP': 37.0,
                                            'SU': 37.0,
                                            'FF': 40.0,
                                            'JF': 0.74999,
                                            'CN': 0.7
                                        }]
                                    },
                                    {
                                        'TMC': {
                                            'PC': 2266,
                                            'DE': 'Avenida Leopoldo Lugones',
                                            'QD': '+',
                                            'LE': 0.59941
                                        },
                                        'SHP': [],
                                        'CF': [{
                                            'TY': 'TR',
                                            'SP': 35.0,
                                            'SU': 35.0,
                                            'FF': 35.1,
                                            'JF': 0.02849,
                                            'CN': 0.7
                                        }]
                                    }
                                ]
                            }
                        ],
                        'mid': '420d330f-57f4-4d4f-94aa-db7c8db748a6',
                        'LI': 'A47-02263',
                        'DE': 'Avenida G Udaondo',
                        'PBT': '2020-03-18T21:13:41Z'
                    }
                ],
                'TY': 'TMC',
                'MAP_VERSION': '202001',
                'EBU_COUNTRY_CODE': 'A',
                'EXTENDED_COUNTRY_CODE': 'A2',
                'TABLE_ID': '47',
                'UNITS': 'metric'
            }],
            'MAP_VERSION': '',
            'CREATED_TIMESTAMP': '2020-03-18T21:13:41.000+0000',
            'VERSION': '3.2',
            'UNITS': 'metric'
        }
