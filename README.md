# Spirograph Generator with Turtle Graphics

A Python application that generates beautiful spirograph patterns using turtle graphics. The program creates complex mathematical curves by simulating circles rolling inside circles.

## What is a Spirograph?

A spirograph is a geometric drawing device that produces mathematical roulette curves called hypotrochoids and epitrochoids. The patterns are created by tracing a point attached to a circle that rolls inside or outside another circle.

## How It Works

This implementation uses a multi-circle rolling system to create complex patterns:

1. **Fixed Circle**: An outer stationary circle with radius `R`
2. **First Rolling Circle**: A circle with radius `r = R/k` that rolls inside the fixed circle
3. **Second Rolling Circle**: A smaller circle with radius `r2 = R/k2` that rolls inside the first rolling circle
4. **Pen Offset**: A pen positioned at distance `h` from the center of the innermost circle

## The Mathematics

The spirograph pattern is generated using parametric equations:

### Position Equations

For a point at time `t`, the position is calculated as:

$$x(t) = (R + r) \cos(t) + (r + r_2) \cos\left(t + \frac{Rt}{r} - \frac{Rt}{pr}\right) + h \cos\left(t + \frac{Rt}{r} - \frac{Rt}{pr} - \frac{Rt}{pr_2}\right)$$

$$y(t) = (R + r) \sin(t) + (r + r_2) \sin\left(t + \frac{Rt}{r} - \frac{Rt}{pr}\right) + h \sin\left(t + \frac{Rt}{r} - \frac{Rt}{pr} - \frac{Rt}{pr_2}\right)$$

Where:
- $R$ = Radius of the fixed outer circle
- $r = R/k$ = Radius of the first rolling circle
- $r_2 = R/k_2$ = Radius of the second rolling circle
- $p$ = Phase parameter affecting the rolling motion
- $h$ = Distance of the pen from the center
- $t$ = Time parameter (angle in radians)

### Parameters Explained

- **R (Radius)**: Controls the overall size of the pattern
- **k (First Ratio)**: Determines the size of the first rolling circle. Higher values create smaller circles and more intricate patterns
- **k2 (Second Ratio)**: Determines the size of the second rolling circle. Affects the complexity of loops
- **p (Phase)**: Modifies the rolling motion phase, creating variations in symmetry
- **h (Pen Distance)**: Controls the amplitude of the pattern. Larger values create larger loops

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Spirograph-with-turtle.git
cd Spirograph-with-turtle
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the spirograph generator:

```bash
python spirograph.py
```

### Controls

- **Press 'q'**: Stop drawing and close the window

### Customizing Parameters

You can modify the parameters in the `main()` function in [spirograph.py](spirograph.py) to create different patterns:

```python
R = 80      # Fixed circle radius
k = 1.5     # First rolling circle ratio
k2 = 3.98   # Second rolling circle ratio
p = 0.5     # Phase parameter
h = 100     # Pen distance from center
```

## Examples

Try these parameter combinations for interesting patterns:

| R  | k   | k2   | p   | h   | Description |
|----|-----|------|-----|-----|-------------|
| 80 | 1.5 | 3.98 | 0.5 | 100 | Default: Flowing loops |
| 80 | 2.0 | 4.0  | 0.5 | 90  | Symmetrical flower |
| 80 | 3.0 | 5.0  | 1.0 | 80  | Star pattern |
| 80 | 1.2 | 6.0  | 0.3 | 120 | Complex spiral |

## Technical Details

- **Language**: Python 3.x
- **Graphics Library**: Turtle (built-in Python module)
- **Drawing Speed**: Optimized with smallest step size (0.01) for smooth curves
- **Auto-completion**: Detects when the pattern is complete and stops automatically

## Requirements

- Python 3.6 or higher
- keyboard library (for quit functionality)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Acknowledgments

- Based on the mathematical concept of hypotrochoids and epitrochoids
- Inspired by the classic Spirograph toy invented by Denys Fisher in 1965
