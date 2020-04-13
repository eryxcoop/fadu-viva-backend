from layers.domain.bus.bus_ending_stops import CIUDAD_UNIVERSITARIA_BUS_ENDING_STOPS
from layers.domain.place.base import Place

FADU = Place(latitude=-34.541216, longitude=-58.443897, radius=500,
             bus_ending_stops=CIUDAD_UNIVERSITARIA_BUS_ENDING_STOPS)

AV_LUGONES = Place(latitude=-34.543535, longitude=-58.446340, radius=200,
                   main_street="Avenida Leopoldo Lugones",
                   first_crossing_street="Avenida Int Güiraldes",
                   second_crossing_street="Avenida G Udaondo")
