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
Module for controlling living room lights in a smart home environment.

This module provides a specialized lights switch implementation for living room
lighting control through the LivingRoomLightsSwitch class, which extends the base
LightsSwitch functionality for this specific location.
"""
from coded_tools.smart_home_onf.lights_switch import LightsSwitch


class LivingRoomLightsSwitch(LightsSwitch):
    """
    CodedTool implementation specifically for living room lights.

    This class extends the base LightsSwitch class to provide functionality
    for controlling living room area lighting. It inherits all methods from
    the parent class but initializes with the specific "Living room" location.
    """

    def __init__(self):
        """
        Constructs a switch for living room lights.

        Initializes a lights switch specifically for the living room area by calling
        the parent class constructor with "Living room" as the location parameter.
        """
        super().__init__("Living room")
