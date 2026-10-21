# -*- coding: utf-8 -*-
"""
Module defining chapter 3 data: Công và Năng lượng
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

CH3 = {
    "id": 3,
    "num": 3,
    "part": "Phần I — Cơ học",
    "title": "Công và Năng lượng",
    "tag": "Định lý Động năng & Thế năng",
    "status": "ready",
    "summary": "Nghiên cứu công cơ học, công suất, định lý biến thiên động năng, trường lực thế, thế năng, định luật bảo toàn cơ năng và khảo sát chuyển động qua đường cong thế năng.",
    "nature": {
        "why": "Trong nhiều bài toán thực tế, lực tác dụng biến đổi phức tạp theo tọa độ hoặc quỹ đạo cong, việc giải trực tiếp phương trình vi phân vector Newton $\\vec{F} = m\\vec{a}$ gặp rất nhiều khó khăn. Phương pháp năng lượng sử dụng các đại lượng vô hướng (công, động năng, thế năng) cho phép liên hệ trực tiếp giữa vận tốc và vị trí mà không cần tích phân theo thời gian.",
        "meaning": "Năng lượng là đại lượng vô hướng đặc trưng cho khả năng sinh công của hệ. Công cơ học là số đo năng lượng được truyền tải hoặc biến đổi qua tương tác cơ học. Lực thế (như trọng lực, đàn hồi, hấp dẫn) có công không phụ thuộc hình dạng đường đi, chỉ phụ thuộc vị trí đầu và cuối, cho phép định nghĩa hàm thế năng. Định luật bảo toàn cơ năng là biểu hiện của tính đối xứng tịnh tiến của thời gian (theo định lý Noether).",
        "conditions": "Cơ năng toàn phần $E = K + U$ chỉ bảo toàn tuyệt đối khi hệ là hệ kín (cô lập) và chỉ có các lực thế tương tác nội bộ. Nếu có ngoại lực hoặc lực không thế (ma sát, lực cản), độ biến thiên cơ năng đúng bằng công của các lực không thế: $\\Delta E = A_{kt}$.",
        "limits": "Khi có ma sát trượt hoặc va chạm không đàn hồi, cơ năng không còn bảo toàn mà chuyển hóa thành nội năng (nhiệt năng). Khi đó cần mở rộng sang Nguyên lý I Nhiệt động lực học."
    },
    "formulas": [
        {
            "name": "Công cơ học và Công suất",
            "latex": "A_{12} = \\int_1^2 \\vec{F} \\cdot d\\vec{r} = \\int_1^2 (F_x dx + F_y dy + F_z dz); \\quad P = \\frac{\\delta A}{dt} = \\vec{F} \\cdot \\vec{v}",
            "meaning": "Công là tích phân đường của lực dọc theo quỹ đạo. Công suất $P$ biểu thị tốc độ sinh công tức thời. Lực vuông góc với độ dời (như lực hướng tâm, phản lực pháp tuyến) không sinh công ($A = 0$).",
            "proof": [
                {"step": "\\delta A = \\vec{F} \\cdot d\\vec{r} = F \\cos\\theta \\, ds", "reason": "Định nghĩa công nguyên tố vi phân khi chất điểm dịch chuyển vi cấp dr"},
                {"step": "A_{12} = \\int_1^2 \\vec{F} \\cdot d\\vec{r}", "reason": "Lấy tích phân cộng dồn công trên toàn bộ quỹ đạo cong từ điểm 1 đến điểm 2"},
                {"step": "\\vec{F} = F_x\\vec{i} + F_y\\vec{j} + F_z\\vec{k}, \\quad d\\vec{r} = dx\\vec{i} + dy\\vec{j} + dz\\vec{k}", "reason": "Biểu diễn vectơ lực và vi phân độ dời trong hệ tọa độ Descartes"},
                {"step": "A_{12} = \\int_1^2 (F_x dx + F_y dy + F_z dz)", "reason": "Khai triển tích vô hướng trong cơ sở trực chuẩn Oxyz"},
                {"step": "P = \\frac{\\delta A}{dt} = \\frac{\\vec{F} \\cdot d\\vec{r}}{dt} = \\vec{F} \\cdot \\frac{d\\vec{r}}{dt} = \\vec{F} \\cdot \\vec{v}", "reason": "Định nghĩa công suất tức thời theo đạo hàm thời gian của công"}
            ],
            "svg": '<svg viewBox="0 0 360 160" class="svg-diagram"><defs><marker id="arrF3" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#6366f1"/></marker><marker id="arrDr3" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/></marker></defs><path d="M 30 130 Q 150 40 320 90" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4"/><circle cx="150" cy="75" r="4" fill="#1e293b"/><line x1="150" y1="75" x2="230" y2="70" stroke="#10b981" stroke-width="3" marker-end="url(#arrDr3)"/><text x="235" y="73" fill="#10b981" font-weight="bold" font-size="13">dr (tiếp tuyến)</text><line x1="150" y1="75" x2="215" y2="25" stroke="#6366f1" stroke-width="3" marker-end="url(#arrF3)"/><text x="220" y="25" fill="#6366f1" font-weight="bold" font-size="13">F</text><path d="M 180 73 A 30 30 0 0 0 175 56" fill="none" stroke="#f59e0b" stroke-width="2"/><text x="185" y="65" fill="#f59e0b" font-size="13">θ</text><text x="60" y="140" fill="#64748b" font-size="12">Quỹ đạo dịch chuyển từ 1 đến 2</text></svg>'
        },
        {
            "name": "Định lý biến thiên Động năng",
            "latex": "A_{tong} = \\Delta K = K_2 - K_1 = \\frac{1}{2}m v_2^2 - \\frac{1}{2}m v_1^2; \\quad K = \\frac{1}{2}m v^2 = \\frac{p^2}{2m}",
            "meaning": "Công của tất cả các lực (kể cả lực thế và lực không thế, nội lực và ngoại lực) tác dụng lên chất điểm bằng độ biến thiên động năng của chất điểm đó.",
            "proof": [
                {"step": "\\delta A = \\vec{F} \\cdot d\\vec{r} = \\left(m \\frac{d\\vec{v}}{dt}\\right) \\cdot (\\vec{v} dt)", "reason": "Áp dụng định luật II Newton F = m dv/dt và vi phân độ dời dr = v dt"},
                {"step": "\\delta A = m \\vec{v} \\cdot d\\vec{v}", "reason": "Giản ước vi phân thời gian dt"},
                {"step": "d(v^2) = d(\\vec{v} \\cdot \\vec{v}) = 2\\vec{v} \\cdot d\\vec{v} \\implies \\vec{v} \\cdot d\\vec{v} = \\frac{1}{2}d(v^2)", "reason": "Vi phân của bình phương vô hướng của vectơ vận tốc"},
                {"step": "\\delta A = m \\cdot \\frac{1}{2}d(v^2) = d\\left(\\frac{1}{2}m v^2\\right) = dK", "reason": "Đưa thừa số m vào trong vi phân và định nghĩa động năng K = 1/2 m v²"},
                {"step": "A_{tong} = \\int_1^2 dK = K_2 - K_1 = \\Delta K", "reason": "Lấy tích phân hai vế từ trạng thái 1 đến trạng thái 2"}
            ]
        },
        {
            "name": "Lực thế, Hàm Thế năng và Bảo toàn Cơ năng",
            "latex": "\\vec{F} = -\\vec{\\nabla} U = -\\text{grad}\\,U; \\quad A_{12} = U_1 - U_2 = -\\Delta U; \\quad E = K + U = \\text{const}",
            "meaning": "Lực thế luôn hướng về phía thế năng giảm nhanh nhất. Công của lực thế bằng độ giảm thế năng. Khi không có lực ma sát hay lực không thế, cơ năng $E = K + U$ là đại lượng bảo toàn.",
            "proof": [
                {"step": "\\oint \\vec{F} \\cdot d\\vec{r} = 0", "reason": "Điều kiện cần và đủ để F là trường lực thế (công trên mọi đường cong kín bằng 0)"},
                {"step": "U(\\vec{r}) = -\\int_{\\vec{r}_0}^{\\vec{r}} \\vec{F} \\cdot d\\vec{r}'", "reason": "Định nghĩa hàm thế năng tại điểm r so với điểm mốc chuẩn r₀"},
                {"step": "dU = -\\vec{F} \\cdot d\\vec{r} = -\\left(\\frac{\\partial U}{\\partial x}dx + \\frac{\\partial U}{\\partial y}dy + \\frac{\\partial U}{\\partial z}dz\\right) \\implies \\vec{F} = -\\text{grad}\\,U", "reason": "So sánh vi phân toàn phần của hàm U(x, y, z)"},
                {"step": "A_{the} = U_1 - U_2 = -\\Delta U", "reason": "Tích phân công của lực thế từ vị trí 1 đến vị trí 2"},
                {"step": "A_{the} + A_{kt} = \\Delta K \\implies -\\Delta U + A_{kt} = \\Delta K \\implies \\Delta(K + U) = A_{kt}", "reason": "Kết hợp với định lý động năng, suy ra định luật biến thiên cơ năng tổng quát"}
            ]
        },
        {
            "name": "Đường cong Thế năng và Dao động nhỏ quanh điểm Cân bằng",
            "latex": "F(x) = -\\frac{dU}{dx}; \\quad \\left.\\frac{dU}{dx}\\right|_{x_0} = 0; \\quad k_{eff} = \\left.\\frac{d^2 U}{dx^2}\\right|_{x_0} > 0 \\implies \\omega = \\sqrt{\\frac{k_{eff}}{m}}",
            "meaning": "Vị trí cân bằng bền là cực tiểu của đường cong thế năng ($U'' > 0$). Khai triển Taylor bậc hai cho thấy mọi dao động nhỏ quanh điểm cân bằng bền đều là dao động điều hòa.",
            "proof": [
                {"step": "F(x) = -U'(x) = 0 \\implies x = x_0", "reason": "Điều kiện lực triệt tiêu xác định vị trí cân bằng của chất điểm"},
                {"step": "U(x) \\approx U(x_0) + U'(x_0)(x - x_0) + \\frac{1}{2}U''(x_0)(x - x_0)^2", "reason": "Khai triển Taylor của hàm thế năng quanh lân cận vị trí cân bằng x₀"},
                {"step": "U(x) \\approx U(x_0) + \\frac{1}{2} k_{eff} (x - x_0)^2, \\quad \\text{với } k_{eff} = U''(x_0)", "reason": "Số hạng bậc nhất triệt tiêu do U'(x₀) = 0"},
                {"step": "F(x) = -\\frac{dU}{dx} = -k_{eff}(x - x_0) \\implies m\\ddot{x} + k_{eff}(x - x_0) = 0", "reason": "Phương trình vi phân tương đương con lắc lò xo độ cứng k_eff"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Tính công của các lực cơ bản và công suất",
            "algorithm": [
                "Bước 1: Xác định lực tác dụng là lực không đổi (dùng $A = F s \\cos\\theta$) hay lực biến đổi (dùng tích phân $A = \\int F_x dx$).",
                "Bước 2: Phân loại lực: Trọng lực ($A = mg(h_1 - h_2)$), Lực đàn hồi ($A = \\frac{1}{2}k x_1^2 - \\frac{1}{2}k x_2^2$), Lực ma sát ($A_{ms} = -\\mu N s$).",
                "Bước 3: Với công suất tức thời dùng $P = \\vec{F}\\cdot\\vec{v} = F v \\cos\\theta$; công suất trung bình dùng $\\bar{P} = A / \\Delta t$.",
                "Bước 4: Kiểm tra dấu của công: Lực phát động sinh công dương ($A > 0$), lực cản/ma sát sinh công âm ($A < 0$)."
            ]
        },
        {
            "name": "Dạng 2: Ứng dụng Định lý Động năng và Bảo toàn Cơ năng",
            "algorithm": [
                "Bước 1: Chọn mốc thế năng thích hợp (thường chọn tại mặt đất hoặc vị trí cân bằng của lò xo).",
                "Bước 2: Xác định trạng thái đầu (1) và trạng thái cuối (2): Viết biểu thức cơ năng $E_1 = K_1 + U_1$ và $E_2 = K_2 + U_2$.",
                "Bước 3: Kiểm tra có lực không thế (ma sát, cản) hay không: Nếu không có $\\implies E_1 = E_2$; Nếu có ma sát $\\implies E_2 - E_1 = A_{ms} = -F_{ms} s$.",
                "Bước 4: Giải phương trình tìm ẩn số (vận tốc $v$, độ cao cực đại $h$, độ nén cực đại của lò xo $\\Delta l$)."
            ]
        },
        {
            "name": "Dạng 3: Bài toán chuyển động trên đường cong và điều kiện không rời quỹ đạo",
            "algorithm": [
                "Bước 1: Sử dụng bảo toàn cơ năng để biểu diễn vận tốc $v$ theo góc lệch $\\theta$ hoặc độ cao $h$.",
                "Bước 2: Viết phương trình định luật II Newton theo phương pháp tuyến hướng tâm: $F_n = m\\frac{v^2}{R}$.",
                "Bước 3: Rút ra biểu thức của phản lực pháp tuyến $N(\\theta)$ hoặc lực căng dây $T(\\theta)$.",
                "Bước 4: Đặt điều kiện không rời quỹ đạo ($N \\ge 0$ hoặc $T \\ge 0$) tại điểm hiểm yếu nhất (thường là đỉnh cao nhất của vòng tròn)."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ 1: Điều kiện để vật trượt hết vòng tròn thẳng đứng",
            "problem": "Một hòn bi nhỏ khối lượng $m$ trượt không vận tốc đầu từ độ cao $h$ trên một đường ray nhẵn không ma sát, sau đó đi vào một vòng lượn tròn thẳng đứng bán kính $R$. Tìm độ cao tối thiểu $h_{min}$ để hòn bi có thể đi qua điểm cao nhất của vòng tròn mà không bị rơi khỏi ray.",
            "analysis": "Hòn bi không rời ray khi phản lực pháp tuyến tại điểm cao nhất $N_{top} \\ge 0$. Ta phối hợp định luật bảo toàn cơ năng (để tìm vận tốc tại đỉnh) và phương trình lực hướng tâm.",
            "solution": "1. Chọn mốc thế năng tại chân vòng tròn ($z = 0$).\\n- Cơ năng ban đầu tại đỉnh dốc:\\n$$E_1 = mgh$$\\n- Cơ năng tại điểm cao nhất của vòng tròn ($z = 2R$):\\n$$E_2 = mg(2R) + \\frac{1}{2}m v_{top}^2$$\\n- Do không có ma sát, cơ năng bảo toàn:\\n$$mgh = 2mgR + \\frac{1}{2}m v_{top}^2 \\implies v_{top}^2 = 2g(h - 2R)$$\\n\\n2. Xét tại điểm cao nhất của vòng tròn:\\nTrọng lực $\\vec{P}$ và phản lực $\\vec{N}$ đều hướng thẳng đứng xuống tâm vòng tròn:\\n$$P + N = m \\frac{v_{top}^2}{R} \\implies mg + N = m \\frac{v_{top}^2}{R} \\implies N = m\\left(\\frac{v_{top}^2}{R} - g\\right)$$\\n\\n3. Điều kiện để bi không rời ray là $N \\ge 0$:\\n$$\\frac{v_{top}^2}{R} \\ge g \\implies v_{top}^2 \\ge gR$$\\n\\n4. Thay biểu thức $v_{top}^2$ vào bất đẳng thức:\\n$$2g(h - 2R) \\ge gR \\implies 2h - 4R \\ge R \\implies 2h \\ge 5R \\implies h \\ge \\frac{5}{2}R = 2.5R$$\\nKết luận: Độ cao thả tối thiểu là $h_{min} = 2.5R$."
        },
        {
            "title": "Ví dụ 2: Lò xo đẩy vật trượt trên mặt sàn có ma sát",
            "problem": "Một vật khối lượng $m = 0.5\\,\\text{kg}$ đặt trên mặt bàn nằm ngang có hệ số ma sát trượt $\\mu = 0.2$. Người ta dùng vật nén một lò xo có độ cứng $k = 200\\,\\text{N/m}$ một đoạn $x_0 = 0.1\\,\\text{m}$ so với trạng thái tự nhiên, rồi buông nhẹ. Lấy $g = 9.8\\,\\text{m/s}^2$. Tìm vận tốc của vật tại thời điểm lò xo vừa đi qua vị trí tự nhiên không biến dạng.",
            "analysis": "Trong giai đoạn từ lúc thả ($x = x_0$) đến khi lò xo về vị trí tự nhiên ($x = 0$), cơ năng giảm dần do công của lực ma sát: $E_2 - E_1 = A_{ms}$.",
            "solution": "1. Cơ năng ban đầu (khi lò xo nén $x_0 = 0.1\\,\\text{m}$, vận tốc $v_1 = 0$):\\n$$E_1 = K_1 + U_1 = 0 + \\frac{1}{2}k x_0^2 = \\frac{1}{2}(200)(0.1)^2 = 1.0\\,\\text{J}$$\\n\\n2. Cơ năng khi lò xo về vị trí tự nhiên ($x = 0$, vận tốc $v_2$):\\n$$E_2 = K_2 + U_2 = \\frac{1}{2}m v_2^2 + 0 = \\frac{1}{2}(0.5) v_2^2 = 0.25 v_2^2$$\\n\\n3. Công của lực ma sát trên đoạn đường dịch chuyển $s = x_0 = 0.1\\,\\text{m}$:\\n$$A_{ms} = -\\mu mg s = -(0.2)(0.5)(9.8)(0.1) = -0.098\\,\\text{J}$$\\n\\n4. Áp dụng định lý biến thiên cơ năng:\\n$$E_2 - E_1 = A_{ms} \\implies 0.25 v_2^2 - 1.0 = -0.098$$\\n$$0.25 v_2^2 = 0.902 \\implies v_2^2 = \\frac{0.902}{0.25} = 3.608$$\\n$$v_2 = \\sqrt{3.608} \\approx 1.899 \\approx 1.90\\,\\text{m/s}$$\\nĐáp số: Vận tốc khi qua vị trí tự nhiên là 1.90 m/s."
        }
    ],
    "pitfalls": [
        {
            "error": "Quên dấu âm trong biểu thức công của lực thế: viết nhầm A = ΔU thay vì A = -ΔU",
            "fix": "Công của lực thế luôn làm giảm thế năng: $A_{12} = U_1 - U_2 = -\\Delta U$. Khi vật rơi từ trên cao xuống, trọng lực sinh công dương ($A > 0$) thì thế năng giảm ($U_1 > U_2$).",
            "tip": "Quy tắc nhẩm: Lực cùng chiều chuyển động $\\to$ sinh công dương $\\to$ tiêu hao thế năng dự trữ."
        },
        {
            "error": "Cho rằng phản lực pháp tuyến N luôn không bao giờ sinh công",
            "fix": "Phản lực $N$ không sinh công khi bề mặt đứng yên. Tuy nhiên, nếu vật trượt trên nêm di động hoặc trong thang máy đang đi lên, bề mặt tiếp xúc di chuyển thì phản lực vẫn sinh công bình thường.",
            "tip": "Chỉ áp dụng $A_N = 0$ khi quỹ đạo của vật hoàn toàn nằm trên mặt tiếp xúc cố định trong hệ quy chiếu khảo sát."
        },
        {
            "error": "Áp dụng định luật bảo toàn cơ năng cho va chạm mềm (va chạm dính)",
            "fix": "Trong va chạm mềm, hai vật dính vào nhau sau va chạm, biến dạng dẻo và ma sát nội phân tử làm cơ năng hao tán cực đại thành nhiệt. Khi đó chỉ có Động lượng bảo toàn, Cơ năng KHÔNG bảo toàn.",
            "tip": "Chỉ dùng bảo toàn động lượng để tìm vận tốc chung ngay sau va chạm, sau đó mới dùng bảo toàn cơ năng cho các chuyển động tiếp theo."
        }
    ],
    "exercises": [
        {
            "id": "ex_3_1",
            "type": "easy",
            "q": "Một hòn đá khối lượng $m = 2\\,\\text{kg}$ rơi thẳng đứng từ độ cao $h_1 = 15\\,\\text{m}$ xuống độ cao $h_2 = 5\\,\\text{m}$ so với mặt đất. Lấy gia tốc trọng trường $g = 9.8\\,\\text{m/s}^2$. Hãy tính công cơ học do trọng lực thực hiện trong quá trình rơi này.",
            "unit": "J",
            "ans": 196.0,
            "tol": 0.05,
            "hints": [
                "Công của trọng lực chỉ phụ thuộc vào hiệu độ cao điểm đầu và điểm cuối: $A = mg(h_1 - h_2)$.",
                "Tính độ biến thiên độ cao: $15 - 5 = 10\\,\\text{m}$."
            ],
            "solution": "Áp dụng công thức công của trọng lực:\\n$$A = mg(h_1 - h_2) = 2 \\times 9.8 \\times (15 - 5) = 2 \\times 9.8 \\times 10 = 196.0\\,\\text{J}$$\\nĐáp số: 196.0 J"
        },
        {
            "id": "ex_3_2",
            "type": "easy",
            "q": "Một chiếc ô tô có khối lượng $m = 1200\\,\\text{kg}$ đang chuyển động trên đường thẳng với vận tốc không đổi $v = 54\\,\\text{km/h}$. Hãy tính động năng của ô tô theo đơn vị Jun (J).",
            "unit": "J",
            "ans": 135000.0,
            "tol": 0.05,
            "hints": [
                "Đổi vận tốc từ km/h sang m/s: $v = 54 / 3.6 = 15\\,\\text{m/s}$.",
                "Áp dụng định nghĩa động năng: $K = \\frac{1}{2}m v^2$."
            ],
            "solution": "1. Đổi đơn vị vận tốc:\\n$$v = 54\\,\\text{km/h} = \\frac{54}{3.6} = 15\\,\\text{m/s}$$\\n2. Động năng của ô tô:\\n$$K = \\frac{1}{2}m v^2 = \\frac{1}{2} \\times 1200 \\times 15^2 = 600 \\times 225 = 135000\\,\\text{J}$$\\nĐáp số: 135000 J"
        },
        {
            "id": "ex_3_3",
            "type": "easy",
            "q": "Một lò xo nhẹ có độ cứng $k = 400\\,\\text{N/m}$ bị nén một đoạn $x = 5\\,\\text{cm} = 0.05\\,\\text{m}$ so với chiều dài tự nhiên. Hãy tính thế năng đàn hồi tích lũy trong lò xo.",
            "unit": "J",
            "ans": 0.5,
            "tol": 0.05,
            "hints": [
                "Công thức tính thế năng đàn hồi lò xo: $U = \\frac{1}{2}k x^2$.",
                "Chú ý đổi độ biến dạng sang mét: $x = 0.05\\,\\text{m}$."
            ],
            "solution": "Áp dụng công thức thế năng đàn hồi:\\n$$U = \\frac{1}{2}k x^2 = \\frac{1}{2} \\times 400 \\times (0.05)^2 = 200 \\times 0.0025 = 0.5\\,\\text{J}$$\\nĐáp số: 0.5 J"
        },
        {
            "id": "ex_3_4",
            "type": "easy",
            "q": "Một xe ô tô chạy thẳng đều với vận tốc $v = 20\\,\\text{m/s}$. Tổng các lực cản tác dụng lên xe là $F_c = 650\\,\\text{N}$. Hãy tính công suất cơ học của động cơ xe theo đơn vị kilôoát (kW).",
            "unit": "kW",
            "ans": 13.0,
            "tol": 0.05,
            "hints": [
                "Khi xe chạy đều, lực kéo của động cơ cân bằng với lực cản: $F_k = F_c = 650\\,\\text{N}$.",
                "Công suất tức thời: $P = F v$. Đổi kết quả từ W sang kW (chia cho 1000)."
            ],
            "solution": "Vì xe chuyển động thẳng đều nên lực kéo động cơ bằng lực cản:\\n$$F = F_c = 650\\,\\text{N}$$\\nCông suất của động cơ:\\n$$P = F \\times v = 650 \\times 20 = 13000\\,\\text{W} = 13.0\\,\\text{kW}$$\\nĐáp số: 13.0 kW"
        },
        {
            "id": "ex_3_5",
            "type": "mid",
            "q": "Một vật khối lượng $m = 3\\,\\text{kg}$ trượt trên sàn nằm ngang với vận tốc ban đầu $v_0 = 8\\,\\text{m/s}$. Hệ số ma sát trượt giữa vật và sàn là $\\mu = 0.25$. Lấy $g = 9.8\\,\\text{m/s}^2$. Sử dụng định lý động năng, tính quãng đường vật trượt được cho đến khi dừng hẳn (làm tròn đến 2 chữ số thập phân).",
            "unit": "m",
            "ans": 13.06,
            "tol": 0.1,
            "hints": [
                "Độ biến thiên động năng: $\\Delta K = 0 - \\frac{1}{2}m v_0^2$.",
                "Công của lực ma sát trượt: $A_{ms} = -F_{ms} s = -\\mu mg s$.",
                "Áp dụng $\\Delta K = A_{ms} \\implies s = \\frac{v_0^2}{2\\mu g}$."
            ],
            "solution": "Theo định lý biến thiên động năng:\\n$$K_2 - K_1 = A_{ms} \\iff 0 - \\frac{1}{2}m v_0^2 = -\\mu mg s$$\\n$$s = \\frac{v_0^2}{2\\mu g} = \\frac{8^2}{2 \\times 0.25 \\times 9.8} = \\frac{64}{4.9} \\approx 13.0612 \\approx 13.06\\,\\text{m}$$\\nĐáp số: 13.06 m"
        },
        {
            "id": "ex_3_6",
            "type": "mid",
            "q": "Một hòn bi nhỏ trượt không vận tốc đầu từ độ cao $h$ xuống một máng cong tròn thẳng đứng bán kính $R = 4\\,\\text{m}$ (bỏ qua mọi ma sát). Để hòn bi có thể vượt qua điểm cao nhất của vòng tròn mà không rơi khỏi máng, độ cao tối thiểu $h_{min}$ phải bằng bao nhiêu mét?",
            "unit": "m",
            "ans": 10.0,
            "tol": 0.1,
            "hints": [
                "Điều kiện để vật không rơi tại đỉnh vòng xiếc: $v_{top}^2 \\ge g R$.",
                "Bảo toàn cơ năng giữa đỉnh dốc và đỉnh vòng xiếc: $mgh = mg(2R) + \\frac{1}{2}m v_{top}^2$.",
                "Suy ra công thức kinh điển $h_{min} = 2.5 R$."
            ],
            "solution": "1. Điều kiện để vật qua đỉnh vòng xiếc mà không rơi:\\n$$N \\ge 0 \\implies v_{top}^2 \\ge g R$$\\n2. Bảo toàn cơ năng giữa điểm thả và đỉnh vòng xiếc:\\n$$mgh = 2mgR + \\frac{1}{2}m v_{top}^2 \\ge 2mgR + \\frac{1}{2}mgR = 2.5 mgR$$\\n$$h_{min} = 2.5 R = 2.5 \\times 4 = 10.0\\,\\text{m}$$\\nĐáp số: 10.0 m"
        },
        {
            "id": "ex_3_7",
            "type": "mid",
            "q": "Một chất điểm chuyển động trong trường lực thế hai chiều có hàm thế năng cho bởi $U(x, y) = 3x^2 y - 5y^2 + 2x$ (đơn vị Jun). Hãy tính công mà trường lực thế này thực hiện khi chất điểm dịch chuyển từ điểm $A(1, 2)$ đến điểm $B(3, 1)$.",
            "unit": "J",
            "ans": -40.0,
            "tol": 0.1,
            "hints": [
                "Công của trường lực thế không phụ thuộc đường đi, chỉ bằng hiệu thế năng: $W = U_A - U_B$.",
                "Tính $U(1, 2)$ và $U(3, 1)$ rồi lấy $U(1, 2) - U(3, 1)$."
            ],
            "solution": "1. Thế năng tại điểm A(1, 2):\\n$$U_A = 3(1^2)(2) - 5(2^2) + 2(1) = 6 - 20 + 2 = -12\\,\\text{J}$$\\n2. Thế năng tại điểm B(3, 1):\\n$$U_B = 3(3^2)(1) - 5(1^2) + 2(3) = 27 - 5 + 6 = 28\\,\\text{J}$$\\n3. Công của trường lực thế:\\n$$W = U_A - U_B = -12 - 28 = -40.0\\,\\text{J}$$\\nĐáp số: -40.0 J"
        },
        {
            "id": "ex_3_8",
            "type": "mid",
            "q": "Một con lắc đơn gồm quả nặng khối lượng $m = 0.5\\,\\text{kg}$ treo trên sợi dây dài $\\ell = 1.2\\,\\text{m}$. Kéo con lắc lệch góc $\\alpha_0 = 60^\\circ$ so với phương thẳng đứng rồi buông nhẹ không vận tốc đầu. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính vận tốc của quả nặng khi nó đi qua vị trí cân bằng thẳng đứng $\\alpha = 0^\\circ$ (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s",
            "ans": 3.43,
            "tol": 0.1,
            "hints": [
                "Chọn mốc thế năng tại vị trí thấp nhất (vị trí cân bằng).",
                "Độ cao ban đầu: $h_0 = \\ell(1 - \\cos\\alpha_0)$.",
                "Bảo toàn cơ năng: $mgh_0 = \\frac{1}{2}mv^2 \\implies v = \\sqrt{2g\\ell(1 - \\cos\\alpha_0)}$."
            ],
            "solution": "Áp dụng định luật bảo toàn cơ năng cho con lắc đơn:\\n$$E_1 = E_2 \\iff mg\\ell(1 - \\cos\\alpha_0) = \\frac{1}{2}m v^2$$\\n$$v = \\sqrt{2g\\ell(1 - \\cos\\alpha_0)}$$\\nThay số với $\\alpha_0 = 60^\\circ$, $\\cos 60^\\circ = 0.5$:\\n$$v = \\sqrt{2 \\times 9.8 \\times 1.2 \\times (1 - 0.5)} = \\sqrt{9.8 \\times 1.2} = \\sqrt{11.76} \\approx 3.4293 \\approx 3.43\\,\\text{m/s}$$\\nĐáp số: 3.43 m/s"
        },
        {
            "id": "ex_3_9",
            "type": "hard",
            "q": "Một hạt có khối lượng $m = 0.2\\,\\text{kg}$ chuyển động một chiều dọc theo trục Ox trong trường thế năng có dạng $U(x) = \\frac{a}{x^2} - \\frac{b}{x}$ với $a = 8\\,\\text{J}\\cdot\\text{m}^2$ và $b = 16\\,\\text{J}\\cdot\\text{m}$. Hãy xác định tần số góc $\\omega$ của dao động nhỏ của hạt quanh vị trí cân bằng bền (rad/s, làm tròn đến 2 chữ số thập phân).",
            "unit": "rad/s",
            "ans": 8.94,
            "tol": 0.1,
            "hints": [
                "Tìm vị trí cân bằng $x_0$ từ phương trình $U'(x) = 0$.",
                "Tính đạo hàm cấp hai $k_{eff} = U''(x_0)$.",
                "Tần số góc dao động nhỏ: $\\omega = \\sqrt{\\frac{k_{eff}}{m}}$."
            ],
            "solution": "1. Lấy đạo hàm cấp 1 của thế năng:\\n$$U'(x) = -\\frac{2a}{x^3} + \\frac{b}{x^2}$$\\nĐiều kiện cân bằng $U'(x_0) = 0$:\\n$$-\\frac{2a}{x_0^3} + \\frac{b}{x_0^2} = 0 \\implies x_0 = \\frac{2a}{b} = \\frac{2 \\times 8}{16} = 1.0\\,\\text{m}$$\\n2. Lấy đạo hàm cấp 2:\\n$$U''(x) = \\frac{6a}{x^4} - \\frac{2b}{x^3}$$\\nTại $x_0 = 1.0\\,\\text{m}$:\\n$$k_{eff} = U''(1.0) = \\frac{6(8)}{1^4} - \\frac{2(16)}{1^3} = 48 - 32 = 16.0\\,\\text{N/m} > 0\\;(\\text{cân bằng bền})$$\\n3. Tần số góc dao động nhỏ:\\n$$\\omega = \\sqrt{\\frac{k_{eff}}{m}} = \\sqrt{\\frac{16}{0.2}} = \\sqrt{80} \\approx 8.944 \\approx 8.94\\,\\text{rad/s}$$\\nĐáp số: 8.94 rad/s"
        },
        {
            "id": "ex_3_10",
            "type": "hard",
            "q": "Một lò xo nhẹ có độ cứng $k = 500\\,\\text{N/m}$ bị nén một đoạn $x_0 = 0.12\\,\\text{m}$ trên mặt sàn nằm ngang. Một vật nhỏ khối lượng $m = 0.4\\,\\text{kg}$ được đặt tì vào đầu lò xo (không gắn chặt). Hệ số ma sát trượt giữa vật và sàn là $\\mu = 0.2$. Lấy $g = 9.8\\,\\text{m/s}^2$. Thả tay để lò xo đẩy vật bung ra. Sau khi rời lò xo tại vị trí tự nhiên, vật tiếp tục trượt thêm một đoạn nữa rồi dừng hẳn. Hãy tính tổng quãng đường $s$ mà vật đã trượt kể từ vị trí ban đầu (làm tròn đến 2 chữ số thập phân).",
            "unit": "m",
            "ans": 4.59,
            "tol": 0.1,
            "hints": [
                "Xét toàn bộ quá trình từ lúc bắt đầu thả ($v_1 = 0$) đến khi dừng hẳn ($v_2 = 0$).",
                "Độ biến thiên cơ năng toàn phần bằng công của lực ma sát trên tổng quãng đường $s$:",
                "$\\Delta E = 0 - \\frac{1}{2}k x_0^2 = -\\mu mg s \\implies s = \\frac{k x_0^2}{2\\mu mg}$."
            ],
            "solution": "Xét trạng thái đầu (vật đứng yên, lò xo nén $x_0$) và trạng thái cuối (vật dừng hẳn, lò xo không biến dạng):\\n- Cơ năng đầu: $E_1 = \\frac{1}{2}k x_0^2$\\n- Cơ năng cuối: $E_2 = 0$\\n- Công của lực ma sát trên toàn bộ quãng đường $s$ là $A_{ms} = -F_{ms} s = -\\mu mg s$.\\nÁp dụng định lý biến thiên cơ năng:\\n$$E_2 - E_1 = A_{ms} \\implies -\\frac{1}{2}k x_0^2 = -\\mu mg s$$\\n$$s = \\frac{k x_0^2}{2\\mu mg}$$\\nThay các số liệu:\\n$$s = \\frac{500 \\times (0.12)^2}{2 \\times 0.2 \\times 0.4 \\times 9.8} = \\frac{500 \\times 0.0144}{1.568} = \\frac{7.2}{1.568} \\approx 4.5918 \\approx 4.59\\,\\text{m}$$\\nĐáp số: 4.59 m"
        }
    ]
}

print("Chapter 3 data module ready.")
