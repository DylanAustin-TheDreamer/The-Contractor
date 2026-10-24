import random


SETTLEMENT_SIZE_RANGES = {
    "village": (0.10, 0.20),
    "town": (0.30, 0.45),
    "small_city": (0.50, 0.70),
    "large_city": (0.70, 0.90),
}
STATION_SIZE_RANGE = (0.35, 0.65)


def make_grid(rows=9, columns=9):
    """Return an empty grid with the requested dimensions."""
    if rows < 1 or columns < 1:
        raise ValueError("rows and columns must be positive")

    return [[0 for _ in range(columns)] for _ in range(rows)]


def generate_city_grid(settlement_type, rows=9, columns=9, rng=None):
    """Generate a connected settlement shape beginning at the grid centre.

    The value 1 represents an area belonging to the settlement. The final
    number of areas is selected from the percentage range for the settlement
    type, and every area is connected to the starting centre cell.
    """
    settlement_type = settlement_type.lower().replace(" ", "_")
    if settlement_type not in SETTLEMENT_SIZE_RANGES:
        valid_types = ", ".join(SETTLEMENT_SIZE_RANGES)
        raise ValueError(f"settlement_type must be one of: {valid_types}")

    minimum, maximum = SETTLEMENT_SIZE_RANGES[settlement_type]
    return _generate_connected_grid(
        minimum, maximum, rows, columns, rng
    )


def generate_station_grid(rows=9, columns=9, rng=None):
    """Generate a connected grid for a space station."""
    minimum, maximum = STATION_SIZE_RANGE
    return _generate_connected_grid(
        minimum, maximum, rows, columns, rng
    )


def _generate_connected_grid(minimum, maximum, rows, columns, rng=None):
    board = make_grid(rows, columns)
    rng = rng or random
    target_percentage = rng.uniform(minimum, maximum)
    target_area_count = max(1, round(rows * columns * target_percentage))

    centre = (rows // 2, columns // 2)
    board[centre[0]][centre[1]] = 1
    occupied = {centre}
    frontier = set(_neighbours(*centre, rows, columns))

    while len(occupied) < target_area_count and frontier:
        position = rng.choice(tuple(frontier))
        frontier.remove(position)
        row, column = position
        board[row][column] = 1
        occupied.add(position)

        for neighbour in _neighbours(row, column, rows, columns):
            if neighbour not in occupied:
                frontier.add(neighbour)

    return board


def _neighbours(row, column, rows, columns):
    """Yield the eight positions surrounding a grid cell."""
    for row_offset in (-1, 0, 1):
        for column_offset in (-1, 0, 1):
            if row_offset == 0 and column_offset == 0:
                continue

            neighbour_row = row + row_offset
            neighbour_column = column + column_offset
            if 0 <= neighbour_row < rows and 0 <= neighbour_column < columns:
                yield neighbour_row, neighbour_column


def generate_grid_pos(posX, posY, board, rng=None):
    """Add one randomly selected neighbouring area to ``board``.

    Return the original board when all cells are already occupied or when the
    supplied position is outside the board.
    """
    rows = len(board)
    columns = len(board[0]) if rows else 0
    if (
        not rows
        or not columns
        or any(len(row) != columns for row in board)
        or not (0 <= posX < rows and 0 <= posY < columns)
    ):
        return board

    available = [
        position
        for position in _neighbours(posX, posY, rows, columns)
        if board[position[0]][position[1]] == 0
    ]
    if available:
        next_row, next_column = (rng or random).choice(available)
        board[next_row][next_column] = 1

    return board


def print_grid(board):
    """Print a grid for quick manual inspection."""
    for row in board:
        print(row)


def start_grid_making(is_station=False):
    """Generate either a station grid or a settlement grid."""
    if is_station:
        return {"board": generate_station_grid()}

    settlement_type = random.choice(tuple(SETTLEMENT_SIZE_RANGES))
    return {
        "settlement_type": settlement_type,
        "board": generate_city_grid(settlement_type)
    }
