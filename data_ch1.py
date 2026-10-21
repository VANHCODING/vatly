# -*- coding: utf-8 -*-
"""
Module defining chapter 1 data: Động học chất điểm
"""

CH1 = {
    "id": 1,
    "num": 1,
    "part": "Phần I — Cơ học",
    "title": "Động học chất điểm",
    "tag": "Vận tốc & Gia tốc",
    "status": "ready",
    "summary": "Mô tả hình học thuần túy của chuyển động theo thời gian: Phương trình quỹ đạo, vận tốc tức thời, gia tốc tiếp tuyến & pháp tuyến, chuyển động ném xiên và tọa độ cực.",
    "nature": {
        "why": "Để hiểu chuyển động, trước hết phải mô tả được vị trí, hướng đi và tốc độ thay đổi của vật trong không gian và thời gian mà chưa cần xét đến lực gây ra chuyển động. Khái niệm 'chất điểm' là mô hình hóa trừu tượng khi kích thước của vật rất nhỏ so với khoảng cách di chuyển.",
        "meaning": "Chuyển động mang tính tương đối; không có chuyển động tuyệt đối mà luôn gắn với một Hệ quy chiếu (vật mốc, hệ trục tọa độ, đồng hồ chuẩn). Vectơ độ dời $\\Delta\\vec{r}$ là biến thiên vị trí đầu-cuối, khác hoàn toàn với quãng đường $s$ là độ dài quỹ đạo. Vectơ vận tốc luôn tiếp tuyến với quỹ đạo. Gia tốc $\\vec{a}$ được phân tích thành 2 thành phần độc lập: gia tốc tiếp tuyến $\\vec{a}_t$ làm biến đổi độ lớn vận tốc (nhanh dần/chậm dần) và gia tốc pháp tuyến $\\vec{a}_n$ bẻ cong quỹ đạo (hướng vào tâm cong).",
        "conditions": "Áp dụng trong phạm vi cơ học cổ điển Newton: Tốc độ $v \\ll c$ (tốc độ ánh sáng), kích thước lớn hơn kích thước nguyên tử vi mô, vật không bị biến dạng và không quay quanh trục riêng của nó.",
        "limits": "Khi chất điểm có kích thước đáng kể và quay (như bánh xe, con quay), mô hình chất điểm không đủ mà phải dùng mô hình hệ chất điểm hoặc vật rắn. Khi tốc độ tiệm cận ánh sáng, phải thay phép biến đổi Galilei bằng phép biến đổi Lorentz của thuyết tương đối."
    },
    "formulas": [
        {
            "name": "Phương trình chuyển động thẳng biến đổi đều",
            "latex": "v = v_0 + at; \\quad x = x_0 + v_0 t + \\frac{1}{2}at^2; \\quad v^2 - v_0^2 = 2a(x - x_0)",
            "meaning": "Mô tả chuyển động trên một đường thẳng có gia tốc $a = \\text{const}$. Hệ thức độc lập thời gian $v^2 - v_0^2 = 2a\\Delta x$ là tiền đề của định lý động năng.",
            "proof": [
                {"step": "a = \\frac{dv}{dt} = \\text{const} \\implies dv = a\\,dt", "reason": "Định nghĩa gia tốc tức thời trong chuyển động thẳng một chiều"},
                {"step": "\\int_{v_0}^v dv' = \\int_0^t a\\,dt' \\implies v - v_0 = at \\implies v = v_0 + at", "reason": "Lấy tích phân xác định hai vế từ t = 0 đến t"},
                {"step": "v = \\frac{dx}{dt} \\implies dx = v\\,dt = (v_0 + at)dt", "reason": "Định nghĩa vận tốc tức thời theo vi phân tọa độ"},
                {"step": "\\int_{x_0}^x dx' = \\int_0^t (v_0 + at')dt' \\implies x - x_0 = v_0 t + \\frac{1}{2}at^2", "reason": "Tích phân hàm đa thức bậc nhất theo biến t"},
                {"step": "a = \\frac{dv}{dt} = \\frac{dv}{dx}\\frac{dx}{dt} = v \\frac{dv}{dx} \\implies v\\,dv = a\\,dx", "reason": "Quy tắc đạo hàm hàm hợp liên hệ trực tiếp giữa v và x"},
                {"step": "\\int_{v_0}^v v' dv' = \\int_{x_0}^x a\\,dx' \\implies \\frac{1}{2}(v^2 - v_0^2) = a(x - x_0)", "reason": "Tích phân hai vế cho ra hệ thức độc lập với thời gian"}
            ]
        },
        {
            "name": "Phân tích gia tốc: Gia tốc tiếp tuyến và pháp tuyến",
            "latex": "\\vec{a} = \\vec{a}_t + \\vec{a}_n; \\quad a_t = \\frac{dv}{dt} = \\frac{d|\\vec{v}|}{dt}; \\quad a_n = \\frac{v^2}{R}; \\quad a = \\sqrt{a_t^2 + a_n^2}",
            "meaning": "Trong quỹ đạo cong bất kỳ, gia tốc toàn phần luôn được tách thành thành phần tiếp tuyến $\\vec{a}_t$ (dọc theo vectơ đơn vị tiếp tuyến $\\vec{\\tau}$) và thành phần pháp tuyến $\\vec{a}_n$ (hướng vào tâm cong theo vectơ đơn vị pháp tuyến $\\vec{n}$). $R$ là bán kính chính khúc (bán kính cong) tại điểm xét.",
            "proof": [
                {"step": "\\vec{v} = v\\vec{\\tau}, \\quad \\text{với } |\\vec{\\tau}| = 1", "reason": "Biểu diễn vectơ vận tốc bằng độ lớn v nhân vectơ đơn vị tiếp tuyến quỹ đạo"},
                {"step": "\\vec{a} = \\frac{d\\vec{v}}{dt} = \\frac{d(v\\vec{\\tau})}{dt} = \\frac{dv}{dt}\\vec{\\tau} + v\\frac{d\\vec{\\tau}}{dt}", "reason": "Đạo hàm của tích một hàm vô hướng v(t) và một hàm vectơ τ(t)"},
                {"step": "|\\vec{\\tau}|^2 = \\vec{\\tau} \\cdot \\vec{\\tau} = 1 \\implies \\frac{d}{dt}(\\vec{\\tau} \\cdot \\vec{\\tau}) = 2\\vec{\\tau} \\cdot \\frac{d\\vec{\\tau}}{dt} = 0", "reason": "Đạo hàm của độ dài không đổi cho thấy đạo hàm của vectơ đơn vị luôn vuông góc với chính nó"},
                {"step": "\\frac{d\\vec{\\tau}}{dt} = \\frac{d\\varphi}{dt}\\vec{n} = \\omega\\vec{n}, \\quad \\text{với } ds = R\\,d\\varphi", "reason": "Góc quay của tiếp tuyến dφ liên hệ với độ dài cung ds qua bán kính cong R"},
                {"step": "\\frac{d\\varphi}{dt} = \\frac{1}{R}\\frac{ds}{dt} = \\frac{v}{R} \\implies \\frac{d\\vec{\\tau}}{dt} = \\frac{v}{R}\\vec{n}", "reason": "Thay tốc độ dài v = ds/dt vào biểu thức tốc độ quay của pháp tuyến"},
                {"step": "\\vec{a} = \\frac{dv}{dt}\\vec{\\tau} + \\frac{v^2}{R}\\vec{n} = \\vec{a}_t + \\vec{a}_n", "reason": "Thay ngược lại vào biểu thức gia tốc, thu được hai thành phần vuông góc đôi một"}
            ],
            "svg": '<svg viewBox="0 0 380 180" class="svg-diagram"><defs><marker id="arrAt" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/></marker><marker id="arrAn" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7"/></marker><marker id="arrA" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/></marker></defs><path d="M 40 150 Q 180 30 340 140" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5,5"/><text x="310" y="160" fill="#94a3b8" font-size="12">Quỹ đạo cong</text><circle cx="180" cy="78" r="4.5" fill="#1e293b"/><line x1="180" y1="78" x2="270" y2="78" stroke="#10b981" stroke-width="3" marker-end="url(#arrAt)"/><text x="275" y="82" fill="#10b981" font-weight="bold" font-size="13">a_t (tiếp tuyến)</text><line x1="180" y1="78" x2="180" y2="155" stroke="#0284c7" stroke-width="3" marker-end="url(#arrAn)"/><text x="185" y="152" fill="#0284c7" font-weight="bold" font-size="13">a_n (pháp tuyến, tâm cong)</text><polygon points="180,78 270,78 270,155 180,155" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3,3"/><line x1="180" y1="78" x2="270" y2="155" stroke="#ef4444" stroke-width="3.5" marker-end="url(#arrA)"/><text x="278" y="158" fill="#ef4444" font-weight="bold" font-size="14">a (toàn phần)</text></svg>'
        },
        {
            "name": "Chuyển động ném xiên trong trường trọng lực",
            "latex": "x(t) = v_0\\cos\\alpha\\cdot t; \\quad y(t) = v_0\\sin\\alpha\\cdot t - \\frac{1}{2}gt^2; \\quad H = \\frac{v_0^2\\sin^2\\alpha}{2g}; \\quad L = \\frac{v_0^2\\sin 2\\alpha}{g}",
            "meaning": "Chuyển động trong mặt phẳng thẳng đứng phân rã thành hai chuyển động độc lập: Theo phương ngang $Ox$ là chuyển động thẳng đều (không có gia tốc, $a_x = 0$), theo phương thẳng đứng $Oy$ là chuyển động biến đổi đều với gia tốc tự do $a_y = -g$.",
            "proof": [
                {"step": "\\vec{a} = -g\\vec{j} \\implies a_x = 0, \\; a_y = -g", "reason": "Trọng lực hướng thẳng đứng xuống dưới, bỏ qua lực cản không khí"},
                {"step": "v_x = v_0\\cos\\alpha, \\; v_y = v_0\\sin\\alpha - gt", "reason": "Tích phân từng thành phần từ vận tốc ban đầu tại t = 0"},
                {"step": "x(t) = v_0\\cos\\alpha\\cdot t, \\; y(t) = v_0\\sin\\alpha\\cdot t - \\frac{1}{2}gt^2", "reason": "Tích phân tiếp theo thời gian với điều kiện ban đầu x(0) = 0, y(0) = 0"},
                {"step": "t = \\frac{x}{v_0\\cos\\alpha} \\implies y = x\\tan\\alpha - \\frac{g}{2v_0^2\\cos^2\\alpha}x^2", "reason": "Khử tham số thời gian t để tìm phương trình quỹ đạo (đường parabol)"},
                {"step": "v_y = 0 \\implies t_H = \\frac{v_0\\sin\\alpha}{g} \\implies H = y(t_H) = \\frac{v_0^2\\sin^2\\alpha}{2g}", "reason": "Tại đỉnh quỹ đạo, thành phần vận tốc thẳng đứng triệt tiêu"},
                {"step": "y = 0 \\implies t_L = 2t_H = \\frac{2v_0\\sin\\alpha}{g} \\implies L = x(t_L) = \\frac{v_0^2(2\\sin\\alpha\\cos\\alpha)}{g} = \\frac{v_0^2\\sin 2\\alpha}{g}", "reason": "Vật chạm đất khi y = 0, áp dụng công thức nhân đôi sin(2α)"}
            ]
        },
        {
            "name": "Vận tốc và gia tốc trong hệ tọa độ cực (r, θ)",
            "latex": "\\vec{v} = \\dot{r}\\vec{e}_r + r\\dot{\\theta}\\vec{e}_\\theta; \\quad \\vec{a} = (\\ddot{r} - r\\dot{\\theta}^2)\\vec{e}_r + (r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta})\\vec{e}_\\theta",
            "meaning": "Hệ tọa độ tự nhiên thích hợp nhất cho các chuyển động quay, lực xuyên tâm (lực hấp dẫn Kepler, dao động con lắc). Đại lượng $2\\dot{r}\\dot{\\theta}$ là gia tốc dạng Coriolis sinh ra do sự biến thiên đồng thời của bán kính và góc quay.",
            "proof": [
                {"step": "\\vec{r} = r\\vec{e}_r, \\quad \\text{với } \\vec{e}_r = \\cos\\theta\\vec{i} + \\sin\\theta\\vec{j}, \\; \\vec{e}_\\theta = -\\sin\\theta\\vec{i} + \\cos\\theta\\vec{j}", "reason": "Định nghĩa vectơ đơn vị xuyên tâm và đơn vị phương vị"},
                {"step": "\\frac{d\\vec{e}_r}{dt} = \\dot{\\theta}\\vec{e}_\\theta, \\quad \\frac{d\\vec{e}_\\theta}{dt} = -\\dot{\\theta}\\vec{e}_r", "reason": "Đạo hàm theo thời gian của các vectơ đơn vị phụ thuộc góc θ(t)"},
                {"step": "\\vec{v} = \\frac{d}{dt}(r\\vec{e}_r) = \\dot{r}\\vec{e}_r + r\\frac{d\\vec{e}_r}{dt} = \\dot{r}\\vec{e}_r + r\\dot{\\theta}\\vec{e}_\\theta", "reason": "Áp dụng đạo hàm tích hàm số"},
                {"step": "\\vec{a} = \\frac{d\\vec{v}}{dt} = \\frac{d}{dt}(\\dot{r}\\vec{e}_r) + \\frac{d}{dt}(r\\dot{\\theta}\\vec{e}_\\theta)", "reason": "Đạo hàm tiếp một lần nữa theo thời gian"},
                {"step": "\\vec{a} = (\\ddot{r}\\vec{e}_r + \\dot{r}\\dot{\\theta}\\vec{e}_\\theta) + (\\dot{r}\\dot{\\theta}\\vec{e}_\\theta + r\\ddot{\\theta}\\vec{e}_\\theta - r\\dot{\\theta}^2\\vec{e}_r)", "reason": "Khai triển đạo hàm từng tích hạng tử"},
                {"step": "\\vec{a} = (\\ddot{r} - r\\dot{\\theta}^2)\\vec{e}_r + (r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta})\\vec{e}_\\theta", "reason": "Gom nhóm theo các vectơ đơn vị er và eθ"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Chuyển động thẳng biến đổi đều và đồ thị vận tốc - thời gian",
            "algorithm": [
                "Bước 1: Chọn hệ quy chiếu: Trục Ox trùng với quỹ đạo chuyển động, chọn gốc tọa độ O và gốc thời gian t = 0 (kèm chiều dương rõ ràng).",
                "Bước 2: Xác định dấu của vận tốc ban đầu $v_0$ và gia tốc $a$ (chuyển động nhanh dần đều thì $a$ cùng dấu với $v$, chậm dần đều thì $a$ trái dấu với $v$).",
                "Bước 3: Viết hệ phương trình $v(t) = v_0 + at$ và $x(t) = x_0 + v_0 t + \\frac{1}{2}at^2$, hoặc hệ thức liên hệ $v^2 - v_0^2 = 2a\\Delta x$.",
                "Bước 4: Giải hệ phương trình và kiểm tra nghiệm vật lý (loại bỏ thời gian âm $t < 0$ hoặc giai đoạn sau khi vật đã dừng hẳn)."
            ]
        },
        {
            "name": "Dạng 2: Bài toán ném ngang và ném xiên (kể cả trên mặt nghiêng)",
            "algorithm": [
                "Bước 1: Thiết lập hệ tọa độ Descartes: Gốc O tại vị trí ném, trục Ox nằm ngang theo chiều ném, trục Oy thẳng đứng hướng lên.",
                "Bước 2: Phân tích vận tốc ban đầu: $v_{0x} = v_0\\cos\\alpha$, $v_{0y} = v_0\\sin\\alpha$; gia tốc: $a_x = 0$, $a_y = -g$.",
                "Bước 3: Viết phương trình chuyển động $x(t)$ và $y(t)$, rút $t = \\frac{x}{v_{0x}}$ để lập phương trình quỹ đạo $y(x)$.",
                "Bước 4: Xác định điều kiện bài toán: Đạt đỉnh cao nhất khi $v_y = 0$; chạm đất khi $y = 0$; chạm sườn dốc nghiêng góc $\\beta$ khi $y = x\\tan\\beta$."
            ]
        },
        {
            "name": "Dạng 3: Chuyển động cong, xác định gia tốc tiếp tuyến, pháp tuyến và bán kính cong",
            "algorithm": [
                "Bước 1: Tìm vectơ vận tốc $\\vec{v}(t) = (v_x, v_y, v_z)$ và độ lớn tốc độ dài $v(t) = \\sqrt{v_x^2 + v_y^2 + v_z^2}$.",
                "Bước 2: Tính gia tốc tiếp tuyến bằng đạo hàm của tốc độ dài: $a_t = \\frac{dv}{dt}$.",
                "Bước 3: Tính vectơ gia tốc toàn phần $\\vec{a}(t) = \\frac{d\\vec{v}}{dt}$ và độ lớn $a = \\sqrt{a_x^2 + a_y^2 + a_z^2}$.",
                "Bước 4: Tìm gia tốc pháp tuyến từ định lý Pythagoras: $a_n = \\sqrt{a^2 - a_t^2}$, sau đó suy ra bán kính cong chính khúc: $R = \\frac{v^2}{a_n}$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ 1: Tìm bán kính cong của quỹ đạo ném xiên",
            "problem": "Một vật được ném từ mặt đất với vận tốc ban đầu $v_0 = 20\\,\\text{m/s}$ hợp với phương ngang một góc $\\alpha = 60^\\circ$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính bán kính cong của quỹ đạo tại vị trí bắt đầu ném và tại điểm cao nhất của quỹ đạo.",
            "analysis": "Bán kính cong được định nghĩa qua gia tốc pháp tuyến: $R = \\frac{v^2}{a_n}$. Ta cần xác định tốc độ dài $v$ và thành phần gia tốc vuông góc với vận tốc $a_n$ tại hai thời điểm tương ứng.",
            "solution": "1. Tại vị trí ném ban đầu ($t = 0$):\\n- Vận tốc: $v = v_0 = 20\\,\\text{m/s}$. Vectơ vận tốc hợp với phương ngang góc $60^\\circ$.\\n- Trọng lực gây gia tốc toàn phần $\\vec{a} = \\vec{g}$ (hướng thẳng đứng xuống dưới).\\n- Vectơ pháp tuyến $\\vec{n}$ vuông góc với tiếp tuyến vận tốc, do đó góc giữa $\\vec{g}$ và $\\vec{n}$ là $(90^\\circ - 60^\\circ) = 30^\\circ$ hoặc góc giữa $\\vec{g}$ và tiếp tuyến là $90^\\circ + 60^\\circ$.\\n- Thành phần pháp tuyến: $a_n = g \\cos\\alpha = 9.8 \\times \\cos(60^\\circ) = 9.8 \\times 0.5 = 4.9\\,\\text{m/s}^2$.\\n- Bán kính cong ban đầu:\\n$$R_0 = \\frac{v_0^2}{a_n} = \\frac{20^2}{4.9} = \\frac{400}{4.9} \\approx 81.63\\,\\text{m}$$\\n\\n2. Tại đỉnh cao nhất của quỹ đạo:\\n- Vận tốc tại đỉnh chỉ còn thành phần nằm ngang: $v_{top} = v_0\\cos\\alpha = 20\\cos(60^\\circ) = 10\\,\\text{m/s}$.\\n- Lúc này vận tốc nằm ngang nên vectơ gia tốc $\\vec{g}$ thẳng đứng hoàn toàn vuông góc với vận tốc $\\implies a_n = g = 9.8\\,\\text{m/s}^2$ (và $a_t = 0$).\\n- Bán kính cong tại đỉnh:\\n$$R_{top} = \\frac{v_{top}^2}{g} = \\frac{10^2}{9.8} = \\frac{100}{9.8} \\approx 10.20\\,\\text{m}$$\\n(Nhận xét: Tại đỉnh quỹ đạo bị bẻ cong gắt nhất nên bán kính cong nhỏ nhất)."
        },
        {
            "title": "Ví dụ 2: Thuyền chuyển động qua sông trong dòng nước chảy",
            "problem": "Một con sông rộng $d = 200\\,\\text{m}$ có dòng nước chảy với vận tốc không đổi $u = 1.5\\,\\text{m/s}$. Một chiếc thuyền chuyển động với tốc độ không đổi $v_t = 2.5\\,\\text{m/s}$ đối với nước. Người lái muốn thuyền đi sang bờ bên kia tại điểm đối diện chính xác với điểm xuất phát. Xác định góc hướng mũi thuyền và thời gian qua sông.",
            "analysis": "Áp dụng công thức cộng vận tốc Galilei: $\\vec{v} = \\vec{v}_t + \\vec{u}$, trong đó $\\vec{v}$ là vận tốc của thuyền đối với bờ sông. Để đến đúng điểm đối diện bờ bên kia, vectơ vận tốc thực tế $\\vec{v}$ phải vuông góc với dòng sông.",
            "solution": "1. Xác định góc lái thuyền:\\nTam giác vận tốc là tam giác vuông tại đỉnh của $\\vec{v}$:\\n$$v = \\sqrt{v_t^2 - u^2} = \\sqrt{2.5^2 - 1.5^2} = \\sqrt{6.25 - 2.25} = \\sqrt{4} = 2.0\\,\\text{m/s}$$\\nMũi thuyền phải chếch ngược dòng nước một góc $\\theta$ so với phương vuông góc dòng sông:\\n$$\\sin\\theta = \\frac{u}{v_t} = \\frac{1.5}{2.5} = 0.6 \\implies \\theta = \\arcsin(0.6) \\approx 36.87^\\circ$$\\n(Nghĩa là mũi thuyền hợp với phương dòng nước chảy góc $90^\\circ + 36.87^\\circ = 126.87^\\circ$).\\n\\n2. Thời gian thuyền qua sông:\\n$$t = \\frac{d}{v} = \\frac{200}{2.0} = 100\\,\\text{giây}$$\\nĐáp số: Mũi thuyền chếch 36.87° về phía ngược dòng; thời gian qua sông là 100 s."
        }
    ],
    "pitfalls": [
        {
            "error": "Nhầm lẫn giữa độ dời |Δr| và quãng đường s",
            "fix": "Độ dời là khoảng cách ngắn nhất giữa điểm đầu và điểm cuối (vectơ). Quãng đường là chiều dài thực tế mà vật đã đi qua (vô hướng, luôn ≥ 0). Quãng đường chỉ bằng độ lớn độ dời khi vật đi thẳng và không bao giờ quay đầu.",
            "tip": "Ví dụ: Đi một vòng tròn bán kính R rồi về điểm xuất phát thì độ dời $\\Delta\\vec{r} = \\vec{0}$, nhưng quãng đường đi được là $s = 2\\pi R$."
        },
        {
            "error": "Nhầm công thức vận tốc trung bình là trung bình cộng hai vận tốc: $v_{tb} = (v_1 + v_2)/2$",
            "fix": "Vận tốc trung bình luôn định nghĩa là $v_{tb} = \\frac{\\text{Tổng quãng đường}}{\\text{Tổng thời gian}} = \\frac{s_1 + s_2}{t_1 + t_2}$. Chỉ khi hai khoảng thời gian bằng nhau ($t_1 = t_2$) thì mới được lấy trung bình cộng.",
            "tip": "Nếu đi 2 nửa quãng đường bằng nhau ($s_1 = s_2$), công thức đúng là trung bình điều hòa: $v_{tb} = \\frac{2 v_1 v_2}{v_1 + v_2}$."
        },
        {
            "error": "Quên dấu trừ của gia tốc trọng trường khi chọn trục Oy hướng lên",
            "fix": "Khi chọn trục Oy hướng lên trên, vectơ trọng trường hướng xuống nên hình chiếu luôn là $a_y = -g$.",
            "tip": "Hãy luôn vẽ trục tọa độ kèm mũi tên chiều dương trước khi viết bất kỳ phương trình động học nào."
        }
    ],
    "exercises": [
        {
            "id": "ex_1_1",
            "type": "easy",
            "q": "Một ô tô chạy trên đoạn đường thẳng dài $120\\,\\text{km}$. Nửa đoạn đường đầu ô tô chạy với vận tốc không đổi $v_1 = 30\\,\\text{km/h}$, nửa đoạn đường sau chạy với $v_2 = 60\\,\\text{km/h}$. Tính vận tốc trung bình của ô tô trên cả chặng đường (km/h).",
            "unit": "km/h",
            "ans": 40.0,
            "tol": 0.05,
            "hints": [
                "Không lấy trung bình cộng $(30 + 60)/2$!",
                "Tính thời gian đi nửa đoạn đầu $t_1 = s_1 / v_1 = 60 / 30$ và nửa đoạn sau $t_2 = 60 / 60$.",
                "Áp dụng $v_{tb} = \\frac{s_{total}}{t_1 + t_2}$."
            ],
            "solution": "Thời gian đi từng chặng:\\n- $t_1 = \\frac{60}{30} = 2\\,\\text{h}$\\n- $t_2 = \\frac{60}{60} = 1\\,\\text{h}$\\nTổng thời gian: $t = t_1 + t_2 = 3\\,\\text{h}$.\\nVận tốc trung bình:\\n$$v_{tb} = \\frac{s}{t} = \\frac{120}{3} = 40\\,\\text{km/h}$$\\nĐáp số: 40 km/h"
        },
        {
            "id": "ex_1_2",
            "type": "easy",
            "q": "Một đoàn tàu đang chạy thẳng đều với vận tốc $v_0 = 20\\,\\text{m/s}$ thì người lái tàu hãm phanh chuyển động chậm dần đều với độ lớn gia tốc $a = 2.5\\,\\text{m/s}^2$. Hãy tính quãng đường mà tàu trượt thêm cho đến khi dừng hẳn.",
            "unit": "m",
            "ans": 80.0,
            "tol": 0.05,
            "hints": [
                "Khi tàu dừng lại, vận tốc cuối $v = 0$.",
                "Dùng hệ thức độc lập với thời gian: $v^2 - v_0^2 = 2 a_{đs} s$ với $a_{đs} = -2.5\\,\\text{m/s}^2$."
            ],
            "solution": "Áp dụng hệ thức độc lập thời gian:\\n$$v^2 - v_0^2 = 2 a s \\implies 0^2 - 20^2 = 2(-2.5) s$$\\n$$-400 = -5 s \\implies s = \\frac{400}{5} = 80\\,\\text{m}$$\\nĐáp số: 80 m"
        },
        {
            "id": "ex_1_3",
            "type": "easy",
            "q": "Một viên sỏi được thả rơi tự do không vận tốc đầu từ tầng thượng một tòa tháp cao $h = 45\\,\\text{m}$. Lấy gia tốc trọng trường $g = 10\\,\\text{m/s}^2$. Bỏ qua sức cản không khí, tính thời gian rơi của viên sỏi cho đến khi chạm đất.",
            "unit": "s",
            "ans": 3.0,
            "tol": 0.05,
            "hints": [
                "Phương trình quãng đường rơi tự do: $h = \\frac{1}{2}gt^2$.",
                "Suy ra công thức thời gian rơi $t = \\sqrt{\\frac{2h}{g}}$."
            ],
            "solution": "Thời gian rơi tự do:\\n$$t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2 \\times 45}{10}} = \\sqrt{\\frac{90}{10}} = \\sqrt{9} = 3\\,\\text{s}$$\\nĐáp số: 3 s"
        },
        {
            "id": "ex_1_4",
            "type": "easy",
            "q": "Một vành bánh xe bán kính $R = 0.5\\,\\text{m}$ đang quay tròn đều với tần số quay $f = 2\\,\\text{vòng/giây}$ (Hz). Lấy $\\pi = 3.1416$. Tính gia tốc hướng tâm của một điểm nằm trên vành bánh xe (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s²",
            "ans": 78.96,
            "tol": 0.5,
            "hints": [
                "Tốc độ góc $\\omega = 2\\pi f$.",
                "Gia tốc hướng tâm $a_n = \\omega^2 R$."
            ],
            "solution": "Tốc độ góc của chuyển động tròn:\\n$$\\omega = 2\\pi f = 2 \\times 3.1416 \\times 2 = 4\\pi \\approx 12.5664\\,\\text{rad/s}$$\\nGia tốc hướng tâm (pháp tuyến):\\n$$a_n = \\omega^2 R = (4\\pi)^2 \\times 0.5 = 16\\pi^2 \\times 0.5 = 8\\pi^2 \\approx 8 \\times 9.8696 = 78.96\\,\\text{m/s}^2$$\\nĐáp số: 78.96 m/s²"
        },
        {
            "id": "ex_1_5",
            "type": "mid",
            "q": "Từ đỉnh một mỏm đá cao $h = 20\\,\\text{m}$ so với mặt biển, người ta ném một hòn đá theo phương nằm ngang với vận tốc ban đầu $v_0 = 15\\,\\text{m/s}$. Lấy $g = 10\\,\\text{m/s}^2$. Hãy tính tầm bay xa theo phương ngang của hòn đá khi nó chạm mặt nước.",
            "unit": "m",
            "ans": 30.0,
            "tol": 0.1,
            "hints": [
                "Thời gian rơi của chuyển động ném ngang bằng thời gian rơi tự do từ độ cao h: $t = \\sqrt{2h/g}$.",
                "Tầm xa tính theo phương ngang là $L = v_0 t$."
            ],
            "solution": "Thời gian chuyển động của hòn đá cho đến khi chạm biển:\\n$$t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{2 \\times 20}{10}} = \\sqrt{4} = 2\\,\\text{s}$$\\nTầm xa theo phương ngang:\\n$$L = v_0 \\times t = 15 \\times 2 = 30\\,\\text{m}$$\\nĐáp số: 30 m"
        },
        {
            "id": "ex_1_6",
            "type": "mid",
            "q": "Một quả cầu được ném xiên từ mặt đất với vận tốc ban đầu $v_0 = 25\\,\\text{m/s}$, góc ném $\\alpha = 30^\\circ$ so với phương ngang. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính độ cao cực đại $H$ mà quả cầu đạt được (làm tròn đến 2 chữ số thập phân).",
            "unit": "m",
            "ans": 7.97,
            "tol": 0.1,
            "hints": [
                "Tại đỉnh cao nhất, thành phần vận tốc thẳng đứng $v_y = 0$.",
                "Áp dụng công thức độ cao cực đại: $H = \\frac{(v_0 \\sin\\alpha)^2}{2g}$."
            ],
            "solution": "Vận tốc thành phần thẳng đứng ban đầu:\\n$$v_{0y} = v_0 \\sin 30^\\circ = 25 \\times 0.5 = 12.5\\,\\text{m/s}$$\\nĐộ cao cực đại của vật:\\n$$H = \\frac{v_{0y}^2}{2g} = \\frac{12.5^2}{2 \\times 9.8} = \\frac{156.25}{19.6} \\approx 7.9719 \\approx 7.97\\,\\text{m}$$\\nĐáp số: 7.97 m"
        },
        {
            "id": "ex_1_7",
            "type": "mid",
            "q": "Một chất điểm chuyển động trên đường tròn bán kính $R = 20\\,\\text{m}$ với phương trình quãng đường đi được là $s(t) = 2t^2$ (m, s). Hãy tính độ lớn gia tốc toàn phần của chất điểm tại thời điểm $t = 2\\,\\text{s}$ (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s²",
            "ans": 5.12,
            "tol": 0.1,
            "hints": [
                "Tìm tốc độ dài tức thời $v(t) = s'(t) = 4t$.",
                "Gia tốc tiếp tuyến $a_t = s''(t) = 4\\,\\text{m/s}^2$.",
                "Gia tốc pháp tuyến $a_n = \\frac{v^2}{R}$.",
                "Gia tốc toàn phần $a = \\sqrt{a_t^2 + a_n^2}$."
            ],
            "solution": "1. Tốc độ dài tại $t = 2\\,\\text{s}$:\\n$$v(t) = \\frac{ds}{dt} = 4t \\implies v(2) = 4 \\times 2 = 8\\,\\text{m/s}$$\\n2. Gia tốc tiếp tuyến:\\n$$a_t = \\frac{dv}{dt} = 4\\,\\text{m/s}^2$$\\n3. Gia tốc pháp tuyến tại $t = 2\\,\\text{s}$:\\n$$a_n = \\frac{v^2}{R} = \\frac{8^2}{20} = \\frac{64}{20} = 3.2\\,\\text{m/s}^2$$\\n4. Gia tốc toàn phần:\\n$$a = \\sqrt{a_t^2 + a_n^2} = \\sqrt{4^2 + 3.2^2} = \\sqrt{16 + 10.24} = \\sqrt{26.24} \\approx 5.1225 \\approx 5.12\\,\\text{m/s}^2$$\\nĐáp số: 5.12 m/s²"
        },
        {
            "id": "ex_1_8",
            "type": "mid",
            "q": "Một vật được ném với vận tốc ban đầu $v_0 = 20\\,\\text{m/s}$, góc ném $\\alpha = 60^\\circ$ so với mặt đất nằm ngang. Lấy $g = 9.8\\,\\text{m/s}^2$. Bỏ qua sức cản không khí, hãy tính bán kính cong $R$ của quỹ đạo tại đỉnh cao nhất (làm tròn đến 2 chữ số thập phân).",
            "unit": "m",
            "ans": 10.20,
            "tol": 0.1,
            "hints": [
                "Tại đỉnh cao nhất, vận tốc chỉ còn thành phần nằm ngang $v = v_0\\cos\\alpha$.",
                "Tại đó, gia tốc trọng trường $\\vec{g}$ vuông góc với vận tốc nên đóng vai trò là gia tốc pháp tuyến $a_n = g$.",
                "Áp dụng công thức bán kính cong $R = \\frac{v^2}{a_n}$."
            ],
            "solution": "Vận tốc tại đỉnh cao nhất của quỹ đạo parabol:\\n$$v_{top} = v_0 \\cos 60^\\circ = 20 \\times 0.5 = 10\\,\\text{m/s}$$\\nTại đỉnh, vectơ vận tốc nằm ngang nên gia tốc pháp tuyến chính bằng gia tốc trọng trường:\\n$$a_n = g = 9.8\\,\\text{m/s}^2$$\\nBán kính cong tại đỉnh:\\n$$R = \\frac{v_{top}^2}{g} = \\frac{10^2}{9.8} = \\frac{100}{9.8} \\approx 10.204 \\approx 10.20\\,\\text{m}$$\\nĐáp số: 10.20 m"
        },
        {
            "id": "ex_1_9",
            "type": "hard",
            "q": "Một sườn dốc nghiêng góc $\\beta = 30^\\circ$ so với phương ngang. Từ chân dốc, người ta ném một vật với vận tốc $v_0 = 20\\,\\text{m/s}$ hợp với mặt đất nằm ngang góc $\\alpha = 60^\\circ$ (nghĩa là hợp với mặt dốc góc $30^\\circ$). Lấy $g = 9.8\\,\\text{m/s}^2$. Tính khoảng cách dọc theo mặt dốc từ điểm ném đến điểm rơi (làm tròn đến 2 chữ số thập phân).",
            "unit": "m",
            "ans": 27.21,
            "tol": 0.2,
            "hints": [
                "Cách 1: Lập phương trình chuyển động ném xiên chuẩn $x(t) = v_0\\cos 60^\\circ t$, $y(t) = v_0\\sin 60^\\circ t - \\frac{1}{2}gt^2$. Phương trình mặt dốc là $y = x\\tan 30^\\circ$. Cho hai phương trình bằng nhau để tìm thời gian chạm dốc t.",
                "Khoảng cách dọc mặt dốc là $d = \\frac{x}{\\cos 30^\\circ}$."
            ],
            "solution": "Phương trình tọa độ Descartes:\\n- $x(t) = 20 \\cos 60^\\circ t = 10 t$\\n- $y(t) = 20 \\sin 60^\\circ t - 4.9 t^2 = 10\\sqrt{3} t - 4.9 t^2$\\nPhương trình sườn dốc qua gốc tọa độ: $y = x \\tan 30^\\circ = \\frac{x}{\\sqrt{3}}$.\\nKhi vật chạm dốc ($t > 0$):\\n$$10\\sqrt{3} t - 4.9 t^2 = \\frac{10 t}{\\sqrt{3}}$$\\n$$4.9 t = 10\\sqrt{3} - \\frac{10}{\\sqrt{3}} = \\frac{20}{\\sqrt{3}} \\approx 11.547$$\\n$$t = \\frac{11.547}{4.9} \\approx 2.3565\\,\\text{s}$$\\nTọa độ chạm dốc theo phương ngang:\\n$$x = 10 \\times 2.3565 = 23.565\\,\\text{m}$$\\nKhoảng cách dọc theo sườn dốc:\\n$$d = \\frac{x}{\\cos 30^\\circ} = \\frac{23.565}{\\frac{\\sqrt{3}}{2}} \\approx \\frac{23.565}{0.866025} \\approx 27.21\\,\\text{m}$$\\nĐáp số: 27.21 m"
        },
        {
            "id": "ex_1_10",
            "type": "hard",
            "q": "Một chất điểm chuyển động trên mặt phẳng với các phương trình tọa độ cực theo thời gian là $r(t) = 2t^2$ (m) và $\\theta(t) = 3t$ (rad). Hãy tính độ lớn vận tốc toàn phần của chất điểm tại thời điểm $t = 1\\,\\text{s}$ (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s",
            "ans": 7.21,
            "tol": 0.1,
            "hints": [
                "Trong hệ tọa độ cực, vectơ vận tốc gồm hai thành phần vuông góc: vận tốc xuyên tâm $v_r = \\dot{r}$ và vận tốc phương vị $v_\\theta = r\\dot{\\theta}$.",
                "Tính $\\dot{r} = 4t$ và $\\dot{\\theta} = 3$. Thay $t = 1$ để tính $v_r$ và $v_\\theta$.",
                "Độ lớn vận tốc toàn phần $v = \\sqrt{v_r^2 + v_\\theta^2}$."
            ],
            "solution": "1. Vận tốc xuyên tâm (radial velocity):\\n$$v_r = \\frac{dr}{dt} = 4t \\implies v_r(1) = 4 \\times 1 = 4\\,\\text{m/s}$$\\n2. Vận tốc phương vị (azimuthal velocity):\\n$$v_\\theta = r \\frac{d\\theta}{dt} = (2t^2) \\times (3) = 6t^2 \\implies v_\\theta(1) = 6 \\times 1^2 = 6\\,\\text{m/s}$$\\n3. Độ lớn vận tốc toàn phần:\\n$$v = \\sqrt{v_r^2 + v_\\theta^2} = \\sqrt{4^2 + 6^2} = \\sqrt{16 + 36} = \\sqrt{52} \\approx 7.2111 \\approx 7.21\\,\\text{m/s}$$\\nĐáp số: 7.21 m/s"
        }
    ]
}

print("Chapter 1 data module ready.")
