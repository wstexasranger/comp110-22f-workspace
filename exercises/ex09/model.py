"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt

__author__ = "730601447"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculates distance between self point and other point."""
        distance: float = sqrt(((other.x - self.x)**2) + ((other.y - self.y)**2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Moves the individual cells."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness = self.sickness + 1
        if self.sickness > 89:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "green"
        elif self.is_immune():
            return "lightblue"
        return "gray"
    
    def contract_disease(self) -> None:
        """Changes the cells sickness state to infected."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Determines if a cell is vulnerable or not."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Determines if a cell is infected."""
        if self.sickness > 0:
            return True
        else:
            return False
    
    def contact_with(self, other: Cell) -> None:
        """Changes a cells state to infected if it touches another infected cell and is vulnerable itself."""
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()
        elif self.is_infected() and other.is_vulnerable():
            other.contract_disease()

    def immunize(self) -> None:
        """Sets the cell to immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns true if immune, false if not."""
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0
    
    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected <= 0 or infected >= cells:
            raise ValueError('Infected cells are either too few, or greater than total population.')
        
        if immune >= cells or immune < 0:
            raise ValueError('Immune cells are greater than total population or is negative.')
        
        if immune + infected > cells:
            raise ValueError('The number of immune and infected cells exceeds the number of cells.')

        self.population = []

        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        
        count: int = 0
        while count < infected:
            self.population[count].contract_disease()
            count = count + 1
        
        count2: int = 0
        while count2 < immune:
            self.population[count + count2].immunize()
            count2 = count2 + 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks if there is contact between self cell and any of all the other calls."""
        N: int = 0
        while N < len(self.population) - 1:
            for other in self.population:
                firstCell: Cell = self.population[N]
                if (Point.distance(firstCell.location, other.location) < constants.CELL_RADIUS and firstCell != other):
                    firstCell.contact_with(other)
            N = N + 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        sick_cells: int = 0
        immune_cells: int = 0
        vulnerable_cells: int = 0
        for cell in self.population:
            if cell.sickness > 0:
                sick_cells = sick_cells + 1
            elif cell.is_immune():
                immune_cells = immune_cells + 1
            elif cell.is_vulnerable():
                vulnerable_cells = vulnerable_cells + 1
        if vulnerable_cells + immune_cells == constants.CELL_COUNT:
            return True