"""Génère les bannières du README de profil (motif « écho », niveaux de gris)."""
W, H = 1280, 320
CX = W / 2

def banner(bg, accent, gray_from, gray_to, n=20, base_w=760, h0=4.0, span=190):
    out = []
    y0 = H / 2 + span / 2
    for k in range(n):
        f = k / (n - 1)
        w = base_w * (1 - f) ** 1.25 + 8
        h = h0 * (1 - f * 0.45)
        y = y0 - span * (1 - (1 - f) ** 1.35)
        if k == 0:
            g, op, h = accent, 1.0, h * 1.25
        else:
            g, op = round(gray_from + (gray_to - gray_from) * f), 1 - f * 0.55
        out.append(f'<rect x="{CX - w / 2:.2f}" y="{y - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" '
                   f'rx="{h / 2:.2f}" fill="rgb({g},{g},{g})" fill-opacity="{op:.3f}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" rx="12" fill="{bg}"/>{"".join(out)}</svg>\n')

open("banner-dark.svg", "w").write(banner("#0D0D0D", 255, 200, 50))
open("banner-light.svg", "w").write(banner("#F4F4F2", 13, 60, 205))
