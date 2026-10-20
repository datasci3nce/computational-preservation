"""Illustrative evaluation of the reported scalar fold normal form.

NOT an NCA simulator. Does not reproduce original checkpoint outputs or empirical
passage-error numbers; prints analytical approximations only.
"""
import math

LAMBDA_STAR = 0.20091324
A_COEFF = -0.05493465
B_COEFF = 0.01169046


def passage_approx(lam: float, width: float = 0.1) -> float:
    """Continuous saddle-node ghost approximation in external decisions.

    Valid in the local bottleneck regime for A=a*(lam-lam*)>0 and b>0.
    """
    if not (math.isfinite(lam) and math.isfinite(width) and width > 0):
        raise ValueError("lambda and width must be finite; width must be positive")
    a = A_COEFF * (lam - LAMBDA_STAR)
    if a <= 0 or B_COEFF <= 0:
        raise ValueError("Approximation requires a*(lambda-lambda_star)>0 and b>0")
    return (2.0 / math.sqrt(a * B_COEFF)) * math.atan(width * math.sqrt(B_COEFF / a))


if __name__ == "__main__":
    print("ILLUSTRATIVE local normal-form times — NOT original NCA data")
    print("lambda\twindow\tpassage_approx_decisions")
    for lam in (0.15, 0.18, 0.19, 0.20):
        print(f"{lam:.3f}\t0.100\t{passage_approx(lam):.6f}")
