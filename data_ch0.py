# -*- coding: utf-8 -*-
"""
Module defining chapter 0 data
"""

CH0 = {
    "id": 0,
    "num": 0,
    "part": "Phần Mở đầu",
    "title": "Công cụ toán học và hệ đơn vị",
    "tag": "Toán & Thứ nguyên",
    "status": "ready",
    "summary": "Nền tảng toán học thiết yếu cho Vật lý đại cương 1: Đại số vectơ, phép tính vi tích phân, khai triển Taylor xấp xỉ và giải tích thứ nguyên.",
    "nature": {
        "why": "Vật lý là khoa học thực nghiệm mô tả tự nhiên bằng các quy luật định lượng. Ngôn ngữ chính xác duy nhất để mô tả trạng thái, biến thiên và tương tác vật lý chính là toán học giải tích và đại số vectơ.",
        "meaning": "Vectơ biểu diễn các đại lượng có định hướng trong không gian (như vận tốc, lực, động lượng). Đạo hàm thể hiện tốc độ biến thiên tức thời tại một điểm/thời điểm. Tích phân biểu diễn sự cộng dồn vô hạn các đại lượng vi mô để tạo nên đại lượng vĩ mô (như công, điện thế, khối lượng). Khai triển Taylor giúp tuyến tính hóa các hệ phi tuyến phức tạp trong lân cận trạng thái cân bằng.",
        "conditions": "Các hàm số vật lý được giả thiết là liên tục và khả vi từng khúc trong miền khảo sát. Khai triển gần đúng bậc nhất chỉ có ý nghĩa khi độ lệch vô cùng nhỏ so với giá trị cơ sở (|x| << 1). Phân tích thứ nguyên bắt buộc các số hạng cộng trừ nhau phải đồng nhất về thứ nguyên.",
        "limits": "Giải tích cổ điển bị giới hạn tại các điểm kỳ dị (như r = 0 trong trường hấp dẫn điểm) và không áp dụng trực tiếp cho các biến đổi nhảy bậc trong vật lý lượng tử nếu không thông qua hàm phân bố hoặc toán tử."
    },
    "formulas": [
        {
            "name": "Tích vô hướng của hai vectơ",
            "latex": "\\vec{A} \\cdot \\vec{B} = |\\vec{A}||\\vec{B}| \\cos\\theta = A_x B_x + A_y B_y + A_z B_z",
            "meaning": "Tích vô hướng đo mức độ 'cùng phương' của hai vectơ; kết quả là một đại lượng vô hướng (scalar). Ứng dụng tiêu biểu: Định nghĩa công cơ học $dW = \\vec{F} \\cdot d\\vec{r}$.",
            "proof": [
                {"step": "\\vec{A} = A_x\\vec{i} + A_y\\vec{j} + A_z\\vec{k}, \\quad \\vec{B} = B_x\\vec{i} + B_y\\vec{j} + B_z\\vec{k}", "reason": "Biểu diễn hai vectơ trong cơ sở trực chuẩn Descartes Oxyz"},
                {"step": "\\vec{A} \\cdot \\vec{B} = (A_x\\vec{i} + A_y\\vec{j} + A_z\\vec{k}) \\cdot (B_x\\vec{i} + B_y\\vec{j} + B_z\\vec{k})", "reason": "Áp dụng tiên đề tính chất phân phối của phép nhân vô hướng với phép cộng vectơ"},
                {"step": "\\vec{i}\\cdot\\vec{i} = \\vec{j}\\cdot\\vec{j} = \\vec{k}\\cdot\\vec{k} = 1 \\cdot 1 \\cdot \\cos 0^\\circ = 1", "reason": "Độ dài vectơ đơn vị bằng 1 và góc giữa hai vectơ cùng hướng bằng 0"},
                {"step": "\\vec{i}\\cdot\\vec{j} = \\vec{j}\\cdot\\vec{k} = \\vec{k}\\cdot\\vec{i} = 1 \\cdot 1 \\cdot \\cos 90^\\circ = 0", "reason": "Các trục tọa độ Descartes vuông góc đôi một nên cos(90°) = 0"},
                {"step": "\\vec{A} \\cdot \\vec{B} = A_x B_x + A_y B_y + A_z B_z", "reason": "Khai triển và triệt tiêu 6 số hạng có tích chéo bằng 0, chỉ còn 3 số hạng bình phương cơ sở"}
            ],
            "svg": '<svg viewBox="0 0 360 160" class="svg-diagram"><defs><marker id="arr1" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#6366f1"/></marker><marker id="arr2" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/></marker></defs><line x1="40" y1="120" x2="260" y2="120" stroke="#6366f1" stroke-width="3" marker-end="url(#arr1)"/><text x="270" y="125" fill="#6366f1" font-weight="bold" font-size="14">A</text><line x1="40" y1="120" x2="190" y2="40" stroke="#10b981" stroke-width="3" marker-end="url(#arr2)"/><text x="195" y="38" fill="#10b981" font-weight="bold" font-size="14">B</text><path d="M 80 120 A 40 40 0 0 0 72 98" fill="none" stroke="#f59e0b" stroke-width="2"/><text x="86" y="110" fill="#f59e0b" font-size="13">θ</text><line x1="190" y1="40" x2="190" y2="120" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/><text x="120" y="140" fill="#94a3b8" font-size="12">B·cosθ (hình chiếu)</text></svg>'
        },
        {
            "name": "Tích có hướng của hai vectơ (Tích vectơ)",
            "latex": "\\vec{C} = \\vec{A} \\times \\vec{B}; \\quad |\\vec{C}| = |\\vec{A}||\\vec{B}| \\sin\\theta; \\quad \\vec{C} \\perp \\text{mp}(\\vec{A},\\vec{B})",
            "meaning": "Tích có hướng sinh ra một vectơ mới vuông góc với mặt phẳng chứa hai vectơ ban đầu; độ lớn bằng diện tích hình bình hành dựng trên hai vectơ. Ứng dụng: Momen lực $\\vec{M} = \\vec{r} \\times \\vec{F}$, momen động lượng $\\vec{L} = \\vec{r} \\times \\vec{p}$, lực từ Lorentz $\\vec{F} = q(\\vec{v} \\times \\vec{B})$.",
            "proof": [
                {"step": "\\vec{C} = (A_y B_z - A_z B_y)\\vec{i} + (A_z B_x - A_x B_z)\\vec{j} + (A_x B_y - A_y B_x)\\vec{k}", "reason": "Quy tắc khai triển định thức ma trận cấp 3 theo hàng đầu tiên"},
                {"step": "\\vec{A} \\times \\vec{B} = -(\\vec{B} \\times \\vec{A})", "reason": "Tính chất phản đối xứng: đổi chỗ hai hàng trong định thức làm đổi dấu"},
                {"step": "|\\vec{C}|^2 = (A_y B_z - A_z B_y)^2 + (A_z B_x - A_x B_z)^2 + (A_x B_y - A_y B_x)^2", "reason": "Độ lớn bình phương của vectơ trong không gian tọa độ Descartes"},
                {"step": "|\\vec{C}|^2 = (A_x^2 + A_y^2 + A_z^2)(B_x^2 + B_y^2 + B_z^2) - (A_x B_x + A_y B_y + A_z B_z)^2", "reason": "Đồng nhất thức Lagrange giữa tích có hướng và tích vô hướng"},
                {"step": "|\\vec{C}|^2 = A^2 B^2 - (AB\\cos\\theta)^2 = A^2 B^2 (1 - \\cos^2\\theta) = A^2 B^2 \\sin^2\\theta", "reason": "Sử dụng hệ thức lượng giác cơ bản sin²θ + cos²θ = 1 và lấy căn bậc hai hai vế"}
            ],
            "svg": '<svg viewBox="0 0 360 170" class="svg-diagram"><defs><marker id="arrC" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/></marker></defs><polygon points="60,130 200,130 260,90 120,90" fill="rgba(99,102,241,0.12)" stroke="#818cf8" stroke-dasharray="3,3"/><line x1="60" y1="130" x2="200" y2="130" stroke="#6366f1" stroke-width="3" marker-end="url(#arr1)"/><text x="208" y="135" fill="#6366f1" font-weight="bold" font-size="13">A</text><line x1="60" y1="130" x2="120" y2="90" stroke="#10b981" stroke-width="3" marker-end="url(#arr2)"/><text x="105" y="85" fill="#10b981" font-weight="bold" font-size="13">B</text><line x1="60" y1="130" x2="60" y2="25" stroke="#ef4444" stroke-width="3.5" marker-end="url(#arrC)"/><text x="45" y="22" fill="#ef4444" font-weight="bold" font-size="14">C = A × B</text><text x="145" y="110" fill="#64748b" font-size="12">Diện tích = |A × B|</text></svg>'
        },
        {
            "name": "Khai triển gần đúng Taylor bậc nhất và bậc hai (|x| << 1)",
            "latex": "(1 + x)^n \\approx 1 + nx + \\frac{n(n-1)}{2}x^2; \\quad \\sin x \\approx x - \\frac{x^3}{6}; \\quad \\cos x \\approx 1 - \\frac{x^2}{2}; \\quad e^x \\approx 1 + x",
            "meaning": "Công cụ xấp xỉ chuyển phương trình phi tuyến thành tuyến tính, cho phép giải tích các dao động nhỏ, hiệu ứng tương đối tính ở tốc độ chậm $v \\ll c$, khí thực mật độ thấp.",
            "proof": [
                {"step": "f(x) = f(0) + \\frac{f'(0)}{1!}x + \\frac{f''(0)}{2!}x^2 + \\cdots + \\frac{f^{(n)}(0)}{n!}x^n + R_n(x)", "reason": "Định lý chuỗi Taylor-Maclaurin với hàm f khả vi vô hạn lần quanh lân cận x = 0"},
                {"step": "f(x) = (1+x)^n \\implies f'(x) = n(1+x)^{n-1}, \\; f''(x) = n(n-1)(1+x)^{n-2}", "reason": "Lấy đạo hàm cấp 1 và cấp 2 theo quy tắc hàm lũy thừa"},
                {"step": "f(0) = 1, \\; f'(0) = n, \\; f''(0) = n(n-1)", "reason": "Thay giá trị x = 0 vào các biểu thức đạo hàm"},
                {"step": "(1+x)^n = 1 + nx + \\frac{n(n-1)}{2}x^2 + O(x^3) \\approx 1 + nx", "reason": "Bỏ qua các số hạng bậc 2 trở lên khi |x| rất nhỏ so với 1"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Các phép toán vectơ và hình học giải tích",
            "algorithm": [
                "Bước 1: Phân tích các vectơ theo các thành phần tọa độ trên hệ trục Oxyz: $\\vec{A} = (A_x, A_y, A_z)$.",
                "Bước 2: Dùng tích vô hướng $\\vec{A}\\cdot\\vec{B} = A_x B_x + A_y B_y + A_z B_z$ để tìm công, góc giữa hai vectơ $\\cos\\alpha = \\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{A}||\\vec{B}|}$.",
                "Bước 3: Dùng tích có hướng $\\vec{A}\\times\\vec{B}$ để tìm vectơ vuông góc, diện tích hình bình hành $S = |\\vec{A}\\times\\vec{B}|$ hoặc momen xoay.",
                "Bước 4: Kiểm tra tính trực chuẩn và thứ nguyên của đại lượng tính được."
            ]
        },
        {
            "name": "Dạng 2: Ứng dụng vi tích phân trong chuyển động một chiều và nhiều chiều",
            "algorithm": [
                "Bước 1: Xác định bài toán thuận (biết tọa độ $x(t) \\to$ đạo hàm tìm $v(t) = x'(t), a(t) = v'(t)$) hay bài toán nghịch (biết $a(t) \\to$ tích phân tìm $v(t) = v_0 + \\int a\\,dt, x(t) = x_0 + \\int v\\,dt$).",
                "Bước 2: Nếu gia tốc phụ thuộc vị trí $a(x)$, đổi biến $a = v\\frac{dv}{dx} \\implies \\int v\\,dv = \\int a(x)\\,dx$.",
                "Bước 3: Thay điều kiện biên (điều kiện ban đầu tại $t=0$: $x_0, v_0$) để tìm chính xác hằng số tích phân $C$.",
                "Bước 4: Kiểm tra thứ nguyên kết quả (đơn vị m, m/s, m/s²)."
            ]
        },
        {
            "name": "Dạng 3: Dự đoán công thức vật lý bằng giải tích thứ nguyên (Định lý Pi)",
            "algorithm": [
                "Bước 1: Liệt kê đại lượng cần tìm $Y$ và tất cả các đại lượng vật lý ảnh hưởng $X_1, X_2, ..., X_n$.",
                "Bước 2: Thiết lập phương trình ẩn mũ: $Y = C \\cdot X_1^a \\cdot X_2^b \\cdots X_n^k$, trong đó $C$ là hằng số không thứ nguyên.",
                "Bước 3: Thay thứ nguyên cơ sở của từng đại lượng theo hệ SI: Chiều dài $[L]$, Khối lượng $[M]$, Thời gian $[T]$.",
                "Bước 4: Đồng nhất số mũ của $M, L, T$ ở hai vế để thiết lập hệ phương trình đại số tuyến tính và giải tìm các ẩn $a, b, ..., k$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ 1: Tìm góc giữa hai lực và công cơ học",
            "problem": "Một lực $\\vec{F} = (4\\vec{i} + 3\\vec{j} - 2\\vec{k})$ (N) tác dụng lên chất điểm làm chất điểm dịch chuyển độ dời $\\Delta\\vec{r} = (2\\vec{i} - \\vec{j} + 5\\vec{k})$ (m). Tính công cơ học do lực sinh ra và góc giữa vectơ lực với vectơ độ dời.",
            "analysis": "Công của lực không đổi là tích vô hướng: $W = \\vec{F} \\cdot \\Delta\\vec{r}$. Góc hợp bởi hai vectơ tính thông qua định nghĩa $\\cos\\theta = \\frac{\\vec{F}\\cdot\\Delta\\vec{r}}{|\\vec{F}||\\Delta\\vec{r}|}$.",
            "solution": "1. Tính công $W$:\\n$$W = F_x \\Delta x + F_y \\Delta y + F_z \\Delta z = (4)(2) + (3)(-1) + (-2)(5) = 8 - 3 - 10 = -5\\,\\text{J}$$\\n(Công âm cho thấy lực đóng vai trò cản trở chuyển động).\\n\\n2. Tính độ lớn hai vectơ:\\n- $|\\vec{F}| = \\sqrt{4^2 + 3^2 + (-2)^2} = \\sqrt{16 + 9 + 4} = \\sqrt{29} \\approx 5.385\\,\\text{N}$\\n- $|\\Delta\\vec{r}| = \\sqrt{2^2 + (-1)^2 + 5^2} = \\sqrt{4 + 1 + 25} = \\sqrt{30} \\approx 5.477\\,\\text{m}$\\n\\n3. Tính góc $\\theta$:\\n$$\\cos\\theta = \\frac{W}{|\\vec{F}||\\Delta\\vec{r}|} = \\frac{-5}{\\sqrt{29}\\sqrt{30}} = \\frac{-5}{\\sqrt{870}} \\approx \\frac{-5}{29.496} \\approx -0.1695$$\\n$$\\implies \\theta = \\arccos(-0.1695) \\approx 99.76^\\circ$$"
        },
        {
            "title": "Ví dụ 2: Khai triển Taylor tìm chu kỳ dao động nhỏ",
            "problem": "Thế năng của một hạt trong trường lực một chiều có dạng $U(x) = U_0 \\left[ \\left(\\frac{a}{x}\\right)^{12} - 2\\left(\\frac{a}{x}\\right)^6 \\right]$ (thế Lennard-Jones). Tìm vị trí cân bằng bền $x_0$ và tính gần đúng thế năng quanh vị trí cân bằng dưới dạng thế điều hòa bậc 2.",
            "analysis": "Vị trí cân bằng là nghiệm của $U'(x) = 0$. Khai triển Taylor quanh vị trí cân bằng: $U(x) \\approx U(x_0) + U'(x_0)(x - x_0) + \\frac{1}{2}U''(x_0)(x - x_0)^2$. Vì $U'(x_0) = 0$, số hạng điều hòa xuất phát từ đạo hàm cấp 2 $k_{eff} = U''(x_0)$.",
            "solution": "1. Lấy đạo hàm cấp 1:\\n$$U'(x) = U_0 \\left[ -12 \\frac{a^{12}}{x^{13}} + 12 \\frac{a^6}{x^7} \\right] = 12 U_0 \\frac{a^6}{x^{13}} (x^6 - a^6)$$\\nPhương trình $U'(x) = 0 \\implies x_0 = a$.\\n\\n2. Lấy đạo hàm cấp 2 tại $x_0 = a$:\\n$$U''(x) = 12 U_0 \\left[ 156 \\frac{a^{12}}{x^{14}} - 84 \\frac{a^6}{x^8} \\right]$$\\nTại $x = a$: $U''(a) = 12 U_0 \\left[ 156 \\frac{1}{a^2} - 84 \\frac{1}{a^2} \\right] = \\frac{72 U_0}{a^2} > 0$ (cân bằng bền).\\n\\n3. Khai triển Taylor bậc 2 đặt $\\xi = x - a$ ($|\\xi| \\ll a$):\\n$$U(x) \\approx U(a) + \\frac{1}{2} k_{eff} \\xi^2 = -U_0 + \\frac{36 U_0}{a^2} (x - a)^2$$\\nHạt dao động điều hòa quanh $x = a$ với độ cứng hiệu dụng $k_{eff} = \\frac{72 U_0}{a^2}$."
        }
    ],
    "pitfalls": [
        {
            "error": "Quên đổi số đo góc từ độ (deg) sang radian (rad) khi tính xấp xỉ Taylor",
            "fix": "Các công thức vi tích phân và khai triển $\\sin x \\approx x$, $\\tan x \\approx x$ chỉ đúng khi biến số $x$ có đơn vị là radian.",
            "tip": "Khi đề bài cho $\\alpha = 5^\\circ$, hãy đổi: $x = 5 \\times \\frac{\\pi}{180} \\approx 0.08727\\,\\text{rad}$ trước khi thay vào công thức."
        },
        {
            "error": "Nhầm lẫn tính chất giao hoán của tích có hướng: viết $\\vec{A} \\times \\vec{B} = \\vec{B} \\times \\vec{A}$",
            "fix": "Tích có hướng là phép toán phản đối xứng: $\\vec{A} \\times \\vec{B} = - (\\vec{B} \\times \\vec{A})$. Đổi thứ tự sẽ làm đảo ngược chiều vectơ kết quả.",
            "tip": "Sử dụng quy tắc bàn tay phải: khum 4 ngón tay từ vectơ thứ nhất sang vectơ thứ hai, ngón cái choãi ra chỉ chiều của tích có hướng."
        },
        {
            "error": "Không kiểm tra thứ nguyên sau khi giải bài toán tổng quát",
            "fix": "Trước khi bấm số, hãy nhẩm thứ nguyên hai vế. Nếu vế trái là vận tốc $[L T^{-1}]$ mà vế phải ra $[L^2 T^{-1}]$ thì chắc chắn phép biến đổi đã thiếu hoặc thừa biến.",
            "tip": "Ví dụ công thức chu kỳ con lắc $T = 2\\pi \\sqrt{\\ell/g}$: $[\\sqrt{L / (L T^{-2})}] = [\\sqrt{T^2}] = [T]$ (hoàn toàn chuẩn xác)."
        }
    ],
    "exercises": [
        {
            "id": "ex_0_1",
            "type": "easy",
            "q": "Cho hai vectơ trong không gian: $\\vec{A} = 3\\vec{i} - 2\\vec{j} + 6\\vec{k}$ và $\\vec{B} = 4\\vec{i} + 5\\vec{j} - \\vec{k}$. Hãy tính giá trị tích vô hướng $\\vec{A} \\cdot \\vec{B}$.",
            "unit": "",
            "ans": -4.0,
            "tol": 0.01,
            "hints": [
                "Áp dụng biểu thức tọa độ của tích vô hướng: $\\vec{A} \\cdot \\vec{B} = A_x B_x + A_y B_y + A_z B_z$.",
                "Tính từng tích thành phần: $3 \\times 4$, $(-2) \\times 5$, và $6 \\times (-1)$ rồi cộng các kết quả lại."
            ],
            "solution": "Áp dụng công thức giải tích tọa độ tích vô hướng:\\n$$\\vec{A} \\cdot \\vec{B} = (3)(4) + (-2)(5) + (6)(-1) = 12 - 10 - 6 = -4$$\\nĐáp số: -4"
        },
        {
            "id": "ex_0_2",
            "type": "easy",
            "q": "Hai vectơ $\\vec{A}$ và $\\vec{B}$ có độ lớn lần lượt là $A = 5\\,\\text{m}$ và $B = 8\\,\\text{m}$, góc hợp giữa hai vectơ là $\\theta = 30^\\circ$. Hãy tính độ lớn của tích có hướng $|\\vec{A} \\times \\vec{B}|$.",
            "unit": "m²",
            "ans": 20.0,
            "tol": 0.05,
            "hints": [
                "Độ lớn tích có hướng được tính theo công thức $|\\vec{A} \\times \\vec{B}| = AB \\sin\\theta$.",
                "Nhớ rằng $\\sin 30^\\circ = 0.5$."
            ],
            "solution": "Độ lớn tích có hướng:\\n$$|\\vec{A} \\times \\vec{B}| = A B \\sin\\theta = 5 \\times 8 \\times \\sin(30^\\circ) = 40 \\times 0.5 = 20\\,\\text{m}^2$$\\nĐáp số: 20 m²"
        },
        {
            "id": "ex_0_3",
            "type": "easy",
            "q": "Một chất điểm chuyển động dọc theo trục Ox có phương trình tọa độ $x(t) = 4t^3 - 5t + 2$ (m, s). Hãy tính vận tốc tức thời của chất điểm tại thời điểm $t = 2\\,\\text{s}$.",
            "unit": "m/s",
            "ans": 43.0,
            "tol": 0.05,
            "hints": [
                "Vận tốc tức thời là đạo hàm bậc nhất của tọa độ theo thời gian: $v(t) = \\frac{dx}{dt}$.",
                "Lấy đạo hàm của từng hạng tử: $(4t^3)' = 12t^2$, $(-5t)' = -5$, sau đó thay $t = 2$."
            ],
            "solution": "Lấy đạo hàm của tọa độ $x(t)$ theo thời gian:\\n$$v(t) = \\frac{dx}{dt} = 12t^2 - 5$$\\nTại thời điểm $t = 2\\,\\text{s}$:\\n$$v(2) = 12(2^2) - 5 = 12(4) - 5 = 48 - 5 = 43\\,\\text{m/s}$$\\nĐáp số: 43 m/s"
        },
        {
            "id": "ex_0_4",
            "type": "easy",
            "q": "Vận tốc của một vật biến thiên theo thời gian theo quy luật $v(t) = 3t^2 + 2t$ (m/s). Tính quãng đường vật đi được từ thời điểm $t_1 = 0\\,\\text{s}$ đến $t_2 = 3\\,\\text{s}$ (biết vật không đổi chiều chuyển động).",
            "unit": "m",
            "ans": 36.0,
            "tol": 0.05,
            "hints": [
                "Quãng đường là tích phân của vận tốc theo thời gian: $s = \\int_0^3 v(t)\\,dt$.",
                "Tìm nguyên hàm của $3t^2$ là $t^3$ và của $2t$ là $t^2$, sau đó thế cận từ 0 đến 3."
            ],
            "solution": "Quãng đường dịch chuyển từ $t = 0$ đến $t = 3$:\\n$$s = \\int_0^3 (3t^2 + 2t)\\,dt = \\left[ t^3 + t^2 \\right]_0^3 = (3^3 + 3^2) - (0) = 27 + 9 = 36\\,\\text{m}$$\\nĐáp số: 36 m"
        },
        {
            "id": "ex_0_5",
            "type": "mid",
            "q": "Cho hai vectơ $\\vec{A} = 2\\vec{i} + 3\\vec{j} - \\vec{k}$ và $\\vec{B} = -\\vec{i} + 2\\vec{j} + 2\\vec{k}$. Hãy xác định góc hợp bởi hai vectơ này theo đơn vị độ (lấy tròn đến 1 chữ số thập phân).",
            "unit": "độ",
            "ans": 79.7,
            "tol": 0.5,
            "hints": [
                "Tính tích vô hướng $\\vec{A} \\cdot \\vec{B} = A_x B_x + A_y B_y + A_z B_z$.",
                "Tính độ dài hai vectơ $|\vec{A}| = \\sqrt{A_x^2 + A_y^2 + A_z^2}$ và $|\vec{B}|$.",
                "Dùng công thức $\\cos\\theta = \\frac{\\vec{A}\\cdot\\vec{B}}{|\\vec{A}||\\vec{B}|}$ rồi bấm arccos và đổi sang độ."
            ],
            "solution": "1. Tích vô hướng:\\n$$\\vec{A} \\cdot \\vec{B} = (2)(-1) + (3)(2) + (-1)(2) = -2 + 6 - 2 = 2$$\\n2. Độ lớn hai vectơ:\\n$$|\\vec{A}| = \\sqrt{2^2 + 3^2 + (-1)^2} = \\sqrt{4 + 9 + 1} = \\sqrt{14} \\approx 3.7417$$\\n$$|\\vec{B}| = \\sqrt{(-1)^2 + 2^2 + 2^2} = \\sqrt{1 + 4 + 4} = \\sqrt{9} = 3$$\\n3. Góc giữa hai vectơ:\\n$$\\cos\\theta = \\frac{2}{3\\sqrt{14}} = \\frac{2}{11.22497} \\approx 0.17817$$\\n$$\\theta = \\arccos(0.17817) \\approx 79.74^\\circ \\approx 79.7^\\circ$$\\nĐáp số: 79.7 độ"
        },
        {
            "id": "ex_0_6",
            "type": "mid",
            "q": "Sử dụng khai triển Taylor bậc hai $(1 - x)^{-1/2} \\approx 1 + \\frac{1}{2}x + \\frac{3}{8}x^2$, hãy tính giá trị gần đúng của đại lượng $y = \\frac{1}{\\sqrt{1 - 0.04}}$ (làm tròn đến 4 chữ số thập phân).",
            "unit": "",
            "ans": 1.0206,
            "tol": 0.0005,
            "hints": [
                "Ở đây $x = 0.04$. Thay trực tiếp vào đa thức Taylor bậc hai.",
                "Hạng tử bậc 1 là $\\frac{1}{2}(0.04) = 0.02$. Hạng tử bậc 2 là $\\frac{3}{8}(0.04)^2 = \\frac{3}{8}(0.0016) = 0.0006$."
            ],
            "solution": "Áp dụng công thức khai triển với $x = 0.04$:\\n$$y \\approx 1 + \\frac{1}{2}(0.04) + \\frac{3}{8}(0.04)^2$$\\n$$y \\approx 1 + 0.02 + \\frac{3}{8}(0.0016) = 1 + 0.02 + 0.0006 = 1.0206$$\\n(So sánh với giá trị máy tính: $1/\\sqrt{0.96} \\approx 1.02062$, sai số chỉ $0.002\\%$).\\nĐáp số: 1.0206"
        },
        {
            "id": "ex_0_7",
            "type": "mid",
            "q": "Tốc độ truyền sóng ngang trên một sợi dây căng phụ thuộc vào lực căng dây $T$ (đơn vị N) và khối lượng trên một đơn vị chiều dài $\\mu$ (đơn vị kg/m) theo dạng $v = C \\cdot T^a \\cdot \\mu^b$, với $C$ là hằng số không thứ nguyên. Hãy tìm tổng hai số mũ $(a + b)$.",
            "unit": "",
            "ans": 0.0,
            "tol": 0.01,
            "hints": [
                "Thứ nguyên của vận tốc $[v] = \\text{L}\\text{T}^{-1}$.",
                "Lực căng dây $T$ có thứ nguyên lực $[T] = [F] = \\text{M}\\text{L}\\text{T}^{-2}$.",
                "Mật độ dài $[\\mu] = \\text{M}\\text{L}^{-1}$.",
                "Lập hệ phương trình đồng nhất số mũ của M, L, T rồi giải tìm a và b."
            ],
            "solution": "Phương trình thứ nguyên:\\n$$[v] = [T]^a [\\mu]^b \\implies \\text{L}\\text{T}^{-1} = (\\text{M}\\text{L}\\text{T}^{-2})^a (\\text{M}\\text{L}^{-1})^b = \\text{M}^{a+b} \\text{L}^{a-b} \\text{T}^{-2a}$$\\nĐồng nhất số mũ hai vế:\\n1) Số mũ của M: $a + b = 0 \\implies b = -a$\\n2) Số mũ của T: $-2a = -1 \\implies a = 1/2$\\n3) Do đó $b = -1/2$. Kiểm tra với L: $a - b = 1/2 - (-1/2) = 1$ (thỏa mãn).\\nTổng hai số mũ: $a + b = 1/2 + (-1/2) = 0.0$.\\n(Công thức vật lý là $v = \\sqrt{T/\\mu}$).\\nĐáp số: 0.0"
        },
        {
            "id": "ex_0_8",
            "type": "mid",
            "q": "Trong không gian $Oxyz$, cho hai điểm $M(1, 2, 0)$ và $N(3, 0, 4)$. Tính diện tích tam giác $OMN$ (với $O$ là gốc tọa độ). Làm tròn đến 2 chữ số thập phân.",
            "unit": "đvdt",
            "ans": 5.39,
            "tol": 0.05,
            "hints": [
                "Diện tích tam giác $OMN$ bằng một nửa độ lớn tích có hướng của hai vectơ $\\vec{OM}$ và $\\vec{ON}$: $S = \\frac{1}{2} |\\vec{OM} \\times \\vec{ON}|$.",
                "$\\vec{OM} = (1, 2, 0)$, $\\vec{ON} = (3, 0, 4)$. Tính tích có hướng theo định thức."
            ],
            "solution": "Tọa độ các vectơ: $\\vec{OM} = (1, 2, 0)$, $\\vec{ON} = (3, 0, 4)$.\\nTích có hướng:\\n$$\\vec{OM} \\times \\vec{ON} = \\begin{vmatrix} \\vec{i} & \\vec{j} & \\vec{k} \\\\ 1 & 2 & 0 \\\\ 3 & 0 & 4 \\end{vmatrix} = \\vec{i}(8 - 0) - \\vec{j}(4 - 0) + \\vec{k}(0 - 6) = 8\\vec{i} - 4\\vec{j} - 6\\vec{k}$$\\nĐộ lớn tích có hướng:\\n$$|\\vec{OM} \\times \\vec{ON}| = \\sqrt{8^2 + (-4)^2 + (-6)^2} = \\sqrt{64 + 16 + 36} = \\sqrt{116} \\approx 10.7703$$\\nDiện tích tam giác $OMN$:\\n$$S = \\frac{1}{2} \\sqrt{116} \\approx 5.385 \\approx 5.39\\,\\text{đvdt}$$\\nĐáp số: 5.39"
        },
        {
            "id": "ex_0_9",
            "type": "hard",
            "q": "Cho ba vectơ: $\\vec{A} = \\vec{i} + 2\\vec{k}$, $\\vec{B} = 3\\vec{j} + \\vec{k}$, $\\vec{C} = 2\\vec{i} - \\vec{j}$. Tính độ lớn của vectơ tích kép $\\vec{D} = \\vec{A} \\times (\\vec{B} \\times \\vec{C})$. Làm tròn đến 2 chữ số thập phân.",
            "unit": "",
            "ans": 9.17,
            "tol": 0.05,
            "hints": [
                "Có thể tính trực tiếp $\\vec{B} \\times \\vec{C}$ trước, sau đó lấy $\\vec{A} \\times (\\vec{B} \\times \\vec{C})$.",
                "Hoặc dùng công thức phân rã vectơ BAC-CAB: $\\vec{A} \\times (\\vec{B} \\times \\vec{C}) = \\vec{B}(\\vec{A}\\cdot\\vec{C}) - \\vec{C}(\\vec{A}\\cdot\\vec{B})$."
            ],
            "solution": "Cách 1: Tính từng bước\\n$\\vec{B} = (0, 3, 1)$, $\\vec{C} = (2, -1, 0)$.\\n$$\\vec{B} \\times \\vec{C} = (3\\cdot 0 - 1\\cdot(-1))\\vec{i} - (0\\cdot 0 - 1\\cdot 2)\\vec{j} + (0\\cdot(-1) - 3\\cdot 2)\\vec{k} = \\vec{i} + 2\\vec{j} - 6\\vec{k}$$\\nĐặt $\\vec{u} = \\vec{B} \\times \\vec{C} = (1, 2, -6)$, với $\\vec{A} = (1, 0, 2)$:\\n$$\\vec{D} = \\vec{A} \\times \\vec{u} = \\begin{vmatrix} \\vec{i} & \\vec{j} & \\vec{k} \\\\ 1 & 0 & 2 \\\\ 1 & 2 & -6 \\end{vmatrix} = \\vec{i}(0 - 4) - \\vec{j}(-6 - 2) + \\vec{k}(2 - 0) = -4\\vec{i} + 8\\vec{j} + 2\\vec{k}$$\\nĐộ lớn của $\\vec{D}$:\\n$$|\\vec{D}| = \\sqrt{(-4)^2 + 8^2 + 2^2} = \\sqrt{16 + 64 + 4} = \\sqrt{84} \\approx 9.165 \\approx 9.17$$\\nĐáp số: 9.17"
        },
        {
            "id": "ex_0_10",
            "type": "hard",
            "q": "Một lực biến đổi tác dụng dọc theo trục x có biểu thức $F(x) = \\frac{k}{(x + a)^2}$, với $k = 120\\,\\text{N}\\cdot\\text{m}^2$ và $a = 1\\,\\text{m}$. Hãy tính công cơ học mà lực này thực hiện khi vật dịch chuyển từ $x_1 = 0\\,\\text{m}$ đến $x_2 = 3\\,\\text{m}$.",
            "unit": "J",
            "ans": 90.0,
            "tol": 0.1,
            "hints": [
                "Công của lực biến đổi theo tọa độ được tính bằng tích phân xác định: $W = \\int_{x_1}^{x_2} F(x)\\,dx$.",
                "Nguyên hàm của $\\frac{1}{(x+a)^2}$ là $-\\frac{1}{x+a}$. Thế cận từ 0 đến 3."
            ],
            "solution": "Áp dụng định nghĩa công vi tích phân:\\n$$W = \\int_0^3 \\frac{k}{(x + a)^2}\\,dx = k \\left[ -\\frac{1}{x + a} \\right]_0^3 = k \\left( -\\frac{1}{3 + 1} - \\left( -\\frac{1}{0 + 1} \\right) \\right)$$\\n$$W = k \\left( 1 - \\frac{1}{4} \\right) = \\frac{3}{4} k$$\\nThay giá trị $k = 120\\,\\text{N}\\cdot\\text{m}^2$:\\n$$W = \\frac{3}{4} \\times 120 = 90\\,\\text{J}$$\\nĐáp số: 90 J"
        }
    ]
}

print("Chapter 0 data module ready.")
