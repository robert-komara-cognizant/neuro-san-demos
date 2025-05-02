# Copyright (C) 2023-2025 Cognizant Digital Business, Evolutionary AI.
# All Rights Reserved.
# Issued under the Academic Public License.
#
# You can be released from the terms, and requirements of the Academic Public
# License by purchasing a commercial license.
# Purchase of a commercial license is mandatory for any use of the
# neuro-san-demos SDK Software in commercial settings.
#
"""
Module for controlling kitchen lights in a smart home environment.

This module provides a specialized lights switch implementation for kitchen area
lighting control through the KitchenLightsSwitch class, which extends the base
LightsSwitch functionality for this specific location.
"""
from coded_tools.smart_home_onf.lights_switch import LightsSwitch


class KitchenLightsSwitch(LightsSwitch):
    """
    CodedTool implementation specifically for kitchen lights.

    This class extends the base LightsSwitch class to provide functionality
    for controlling kitchen area lighting. It inherits all methods from
    the parent class but initializes with the specific "Kitchen" location.
    """

    def __init__(self):
        """
        Constructs a switch for kitchen lights.

        Initializes a lights switch specifically for the kitchen area by calling
        the parent class constructor with "Kitchen" as the location parameter.
        """
        super().__init__("Kitchen")
