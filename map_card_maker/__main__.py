"""
Map card maker main program

Author: pca - 2019

"""

import argparse
from pathlib import Path
import osmnx as ox

def main(args):
    """The main routine."""

    print(f"Map card maker starting {args.map_location} output: {args.output_location}")

    size = 480
    dpi = 120

    img_folder = args.output_location
    output_format = "png"

    place = args.map_location

    # distance in metres around the location found in the query.
    dist = 1250

    # Adjust the size according to importance.
    street_widths = {'footway': 0.2,
                     'steps': 0.2,
                     'pedestrian': 0.2,
                     'path': 0.2,
                     'track': 0.2,
                     'service': 0.2,
                     'residential': 0.5,
                     'primary': 2.0,
                     'secondary': 1.25,
                     'tertiary': 0.75,
                     'motorway': 3.0}

    fig, ax = ox.plot_figure_ground(address=place, filename=place, network_type='all', dist=dist,
                                    default_width=0.5, street_widths=street_widths, dpi=dpi, edge_color='#333333', bgcolor='w')

    output_file_name = str(img_folder / Path(f"{place}"))
    ox.plot.save_and_show(fig, ax, save=True, show=False, close=True,
                          filename=output_file_name, file_format=output_format, dpi=dpi, axis_off=True)

    print(f"Finished, saved file: {output_file_name}.{output_format}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Map card maker.')
    parser.add_argument("--map_location",
                        type=str,
                        required=True,
                        help="Which location to create a map for")
    parser.add_argument("--output_location",
                        type=Path,
                        required=True,
                        help="Path to the output location")
    args = parser.parse_args()

    main(args)
