# -*- coding: utf-8 -*-
"""
Module defining data for Chapter 6, 7, 8
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

CH6 = {
    "id": 6,
    "num": 6,
    "part": "Phần I — Cơ học",
    "title": "Trường hấp dẫn",
    "tag": "Định lý Gauss & Các định luật Kepler",
    "status": "ready",
    "summary": "Định luật vạn vật hấp dẫn, cường độ trường hấp dẫn, điện thế hấp dẫn, định lý Gauss, chuyển động thiên thể theo 3 định luật Kepler, các vận tốc vũ trụ I và II, phương trình vis-viva.",
    "nature": {
        "why": "Lực hấp dẫn là tương tác cơ bản chi phối quy mô vĩ mô của vũ trụ, giữ các hành tinh quay quanh Mặt Trời và cấu thành các thiên hà. Khảo sát trường hấp dẫn đặt nền tảng cho cơ học thiên thể và ngành hàng không vũ trụ.",
        "meaning": "Khối lượng quán tính (trong định luật II) và khối lượng hấp dẫn (trong định luật hấp dẫn) bằng nhau với độ chính xác thực nghiệm cực cao (Nguyên lý tương đương của Einstein). Trường hấp dẫn là một trường thế xuyên tâm, bảo toàn momen động lượng dẫn đến định luật diện tích Kepler II. Định lý Gauss là công cụ giải tích mạnh mẽ để tìm cường độ trường của các vật thể phân bố khối lượng đối xứng cầu.",
        "conditions": "Áp dụng trong phạm vi trường hấp dẫn yếu của cơ học Newton ($GM/(r c^2) \\ll 1$) và vận tốc các thiên thể nhỏ hơn nhiều tốc độ ánh sáng.",
        "limits": "Khi trường hấp dẫn cực mạnh (lỗ đen, sao neutron) hoặc hiệu ứng dịch chuyển điểm cận nhật của sao Thủy, lực hấp dẫn Newton không còn chính xác mà phải thay thế bằng độ cong không - thời gian trong Thuyết tương đối rộng."
    },
    "formulas": [
        {
            "name": "Định luật Vạn vật Hấp dẫn và Cường độ trường",
            "latex": "F = G\\frac{m_1 m_2}{r^2}; \\quad \\vec{g} = -\\frac{GM}{r^2}\\vec{e}_r = -\\vec{\\nabla}V; \\quad V(r) = -\\frac{GM}{r}",
            "meaning": "Lực hút xuyên tâm giữa hai chất điểm tỷ lệ nghịch với bình phương khoảng cách. $V(r)$ là thế hấp dẫn (chọn mốc $V(\\infty) = 0$).",
            "proof": [
                {"step": "\\vec{F}_{12} = -G\\frac{m_1 m_2}{r^2}\\vec{e}_r", "reason": "Phát biểu toán học định luật Newton với vectơ đơn vị er hướng từ vật 2 sang vật 1"},
                {"step": "\\vec{g} = \\frac{\\vec{F}}{m} = -\\frac{GM}{r^2}\\vec{e}_r", "reason": "Định nghĩa cường độ trường hấp dẫn (gia tốc rơi tự do)"},
                {"step": "\\vec{\\nabla} \\times \\vec{g} = \\vec{0}", "reason": "Trường xuyên tâm là trường thế, rot bằng 0"},
                {"step": "V(r) = -\\int_\\infty^r g(r')dr' = -\\int_\\infty^r \\frac{GM}{r'^2}dr' = -\\frac{GM}{r}", "reason": "Tích phân xác định thế hấp dẫn với mốc ở vô cực"}
            ]
        },
        {
            "name": "Định lý Gauss cho Trường Hấp dẫn và Định lý vỏ cầu",
            "latex": "\\oint_S \\vec{g} \\cdot d\\vec{A} = -4\\pi G M_{trong}; \\quad g(r) = \\begin{cases} \\frac{GM}{r^2} & (r \\ge R) \\\\ \\frac{GM}{R^3}r & (r < R) \\end{cases}",
            "meaning": "Thông lượng trọng trường qua mặt kín tỷ lệ với khối lượng chứa bên trong. Bên trong khối cầu đặc đồng chất, trọng trường tỷ lệ thuận với bán kính $r$, tạo nên dao động điều hòa nếu đào đường hầm xuyên tâm.",
            "proof": [
                {"step": "\\oint_S \\vec{g} \\cdot d\\vec{A} = g(r) \\cdot 4\\pi r^2", "reason": "Chọn mặt Gauss là mặt cầu đồng tâm bán kính r có g vuông góc và độ lớn không đổi"},
                {"step": "M(r) = M\\frac{r^3}{R^3} \\quad (r < R)", "reason": "Khối lượng khối cầu nằm trong bán kính r tỷ lệ với thể tích"},
                {"step": "g(r) \\cdot 4\\pi r^2 = -4\\pi G \\left(M\\frac{r^3}{R^3}\\right) \\implies g(r) = -\\frac{GM}{R^3}r", "reason": "Áp dụng định lý Gauss và rút gọn thừa số 4πr²"},
                {"step": "F = -m\\left(\\frac{GM}{R^3}\\right)r = -m\\omega^2 r \\implies T = 2\\pi\\sqrt{\\frac{R^3}{GM}} \\approx 84.6\\,\\text{phút}", "reason": "Phương trình vi phân dao động điều hòa xuyên tâm Trái Đất"}
            ]
        },
        {
            "name": "Các Vận tốc Vũ trụ và Định luật Kepler",
            "latex": "v_I = \\sqrt{\\frac{GM}{R}} \\approx 7.9\\,\\text{km/s}; \\quad v_{II} = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2}v_I \\approx 11.2\\,\\text{km/s}; \\quad \\frac{T^2}{a^3} = \\frac{4\\pi^2}{GM}",
            "meaning": "$v_I$ là vận tốc bay trên quỹ đạo tròn sát mặt đất. $v_{II}$ là vận tốc tối thiểu để vật thoát ly hoàn toàn khỏi trường hấp dẫn của hành tinh.",
            "proof": [
                {"step": "m\\frac{v_I^2}{R} = G\\frac{Mm}{R^2} \\implies v_I = \\sqrt{\\frac{GM}{R}} = \\sqrt{g R}", "reason": "Lực hấp dẫn đóng vai trò lực hướng tâm trên quỹ đạo tròn sát mặt đất"},
                {"step": "E = \\frac{1}{2}m v_{II}^2 - G\\frac{Mm}{R} \\ge 0", "reason": "Điều kiện năng lượng để vật bay ra xa vô cùng (E ≥ 0)"},
                {"step": "v_{II} = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2}v_I", "reason": "Vận tốc vũ trụ cấp 2 gấp √2 lần vận tốc cấp 1"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Tính lực hấp dẫn, gia tốc rơi tự do theo độ cao và độ sâu",
            "algorithm": [
                "Bước 1: Trên mặt đất: $g_0 = \\frac{GM}{R^2}$.",
                "Bước 2: Ở độ cao $h$: $g(h) = g_0 \\frac{R^2}{(R+h)^2} \\approx g_0 (1 - \\frac{2h}{R})$ khi $h \\ll R$.",
                "Bước 3: Ở độ sâu $d$ dưới lòng đất: $g(d) = g_0 (1 - \\frac{d}{R})$.",
                "Bước 4: Kiểm tra thứ nguyên gia tốc và giá trị cực đại tại bề mặt $r = R$."
            ]
        },
        {
            "name": "Dạng 2: Chuyển động vệ tinh trên quỹ đạo tròn và địa tĩnh",
            "algorithm": [
                "Bước 1: Viết phương trình lực hướng tâm: $G\\frac{Mm}{r^2} = m\\frac{v^2}{r} = m\\left(\\frac{2\\pi}{T}\\right)^2 r$.",
                "Bước 2: Rút ra vận tốc quỹ đạo $v = \\sqrt{\\frac{GM}{r}}$ và chu kỳ $T = 2\\pi\\sqrt{\\frac{r^3}{GM}}$.",
                "Bước 3: Với vệ tinh địa tĩnh: Đặt $T = 24\\,\\text{h} = 86400\\,\\text{s}$ để tìm bán kính quỹ đạo $r = \\left(\\frac{GM T^2}{4\\pi^2}\\right)^{1/3}$.",
                "Bước 4: Tính độ cao so với mặt đất: $h = r - R$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Tàu vũ trụ chuyển động trên quỹ đạo elip (Phương trình vis-viva)",
            "problem": "Một tàu vũ trụ chuyển động quanh Trái Đất trên quỹ đạo elip có khoảng cách cận địa $r_p = 6800\\,\\text{km}$ và viễn địa $r_a = 42200\\,\\text{km}$. Cho $GM = 3.986 \\times 10^{14}\\,\\text{m}^3/\\text{s}^2$. Tính tốc độ của tàu tại điểm cận địa.",
            "analysis": "Bán trục lớn elip là $a = (r_p + r_a)/2$. Áp dụng phương trình bảo toàn năng lượng vis-viva: $v^2 = GM(2/r - 1/a)$.",
            "solution": "1. Bán trục lớn của elip:\\n$$a = \\frac{r_p + r_a}{2} = \\frac{6800 + 42200}{2} = 24500\\,\\text{km} = 2.45 \\times 10^7\\,\\text{m}$$\\n2. Áp dụng phương trình vis-viva tại điểm cận địa ($r = r_p = 6.8 \\times 10^6\\,\\text{m}$):\\n$$v_p^2 = GM \\left( \\frac{2}{r_p} - \\frac{1}{a} \\right) = 3.986 \\times 10^{14} \\left( \\frac{2}{6.8 \\times 10^6} - \\frac{1}{2.45 \\times 10^7} \\right)$$\\n$$v_p^2 = 3.986 \\times 10^{14} \\left( 2.9412 \\times 10^{-7} - 4.0816 \\times 10^{-8} \\right) = 3.986 \\times 10^{14} \\times 2.5330 \\times 10^{-7} \\approx 1.00965 \\times 10^8$$\\n$$v_p = \\sqrt{1.00965 \\times 10^8} \\approx 10048\\,\\text{m/s} \\approx 10.05\\,\\text{km/s}$$\\nĐáp số: Tốc độ cận địa là 10.05 km/s."
        }
    ],
    "pitfalls": [
        {
            "error": "Nhầm lẫn giữa bán kính quỹ đạo r và độ cao h so với mặt đất",
            "fix": "Bán kính quỹ đạo tính từ tâm Trái Đất: $r = R + h$. Nếu quên cộng bán kính Trái Đất $R \\approx 6400\\,\\text{km}$ thì kết quả sẽ sai lệch nghiêm trọng.",
            "tip": "Luôn luôn vẽ hình từ tâm Trái Đất và ghi chú rõ $r = R_{TD} + h$."
        }
    ],
    "exercises": [
        {
            "id": "ex_6_1",
            "type": "easy",
            "q": "Hai quả cầu chì $m_1 = 50\\,\\text{kg}$ và $m_2 = 80\\,\\text{kg}$ đặt cách nhau $r = 2\\,\\text{m}$. Hằng số hấp dẫn $G = 6.674 \\times 10^{-11}\\,\\text{N}\\cdot\\text{m}^2/\\text{kg}^2$. Tính lực hấp dẫn giữa chúng theo đơn vị $10^{-8}\\,\\text{N}$.",
            "unit": "×10⁻⁸ N",
            "ans": 6.67,
            "tol": 0.05,
            "hints": ["Công thức $F = G \\frac{m_1 m_2}{r^2}$.", "Thay số: $6.674 \\times 10^{-11} \\times 4000 / 4$."],
            "solution": "$$F = 6.674 \\times 10^{-11} \\times \\frac{50 \\times 80}{2^2} = 6.674 \\times 10^{-8}\\,\\text{N}$$\\nĐáp số: 6.67"
        },
        {
            "id": "ex_6_2",
            "type": "easy",
            "q": "Gia tốc trọng trường tại mặt đất là $g_0 = 9.8\\,\\text{m/s}^2$. Tại độ cao $h = R$ (bằng đúng bán kính Trái Đất), gia tốc trọng trường $g$ bằng bao nhiêu m/s²?",
            "unit": "m/s²",
            "ans": 2.45,
            "tol": 0.05,
            "hints": ["Khoảng cách tới tâm Trái Đất là $r = R + h = 2R$.", "Gia tốc giảm tỉ lệ nghịch bình phương: $g = g_0 / 2^2 = g_0 / 4$."],
            "solution": "$$g = g_0 \\frac{R^2}{(2R)^2} = \\frac{9.8}{4} = 2.45\\,\\text{m/s}^2$$\\nĐáp số: 2.45 m/s²"
        },
        {
            "id": "ex_6_3",
            "type": "easy",
            "q": "Cho Trái Đất có $g_0 = 9.8\\,\\text{m/s}^2$ và bán kính $R = 6.4 \\times 10^6\\,\\text{m}$. Tính vận tốc vũ trụ cấp 1 theo đơn vị km/s.",
            "unit": "km/s",
            "ans": 7.92,
            "tol": 0.05,
            "hints": ["$v_I = \\sqrt{g_0 R}$.", "Đổi ra km/s (chia cho 1000)."],
            "solution": "$$v_I = \\sqrt{9.8 \\times 6.4 \\times 10^6} = \\sqrt{6.272 \\times 10^7} \\approx 7919.6\\,\\text{m/s} \\approx 7.92\\,\\text{km/s}$$\\nĐáp số: 7.92 km/s"
        },
        {
            "id": "ex_6_4",
            "type": "easy",
            "q": "Với dữ kiện Trái Đất ở câu trên, hãy tính vận tốc vũ trụ cấp 2 theo đơn vị km/s.",
            "unit": "km/s",
            "ans": 11.2,
            "tol": 0.1,
            "hints": ["$v_{II} = \\sqrt{2} v_I$."],
            "solution": "$$v_{II} = \\sqrt{2} \\times 7.9196 \\approx 11.1999\\,\\text{km/s} \\approx 11.2\\,\\text{km/s}$$\\nĐáp số: 11.2 km/s"
        },
        {
            "id": "ex_6_5",
            "type": "mid",
            "q": "Vệ tinh nhân tạo chuyển động tròn quanh Trái Đất ở độ cao $h = 600\\,\\text{km}$ ($r = 7.0 \\times 10^6\\,\\text{m}$). $M_{TD} = 5.97 \\times 10^{24}\\,\\text{kg}, G = 6.674 \\times 10^{-11}$. Tính chu kỳ quay $T$ của vệ tinh theo phút (làm tròn 2 chữ số).",
            "unit": "phút",
            "ans": 97.16,
            "tol": 0.2,
            "hints": ["$v = \\sqrt{GM/r}$.", "$T = 2\\pi r / v$, đổi từ giây sang phút chia cho 60."],
            "solution": "$$v = \\sqrt{\\frac{6.674 \\times 10^{-11} \\times 5.97 \\times 10^{24}}{7.0 \\times 10^6}} \\approx 7544.5\\,\\text{m/s}$$\\n$$T = \\frac{2\\pi \\times 7.0 \\times 10^6}{7544.5} \\approx 5829.4\\,\\text{s} \\approx 97.16\\,\\text{phút}$$\\nĐáp số: 97.16 phút"
        },
        {
            "id": "ex_6_6",
            "type": "mid",
            "q": "Đưa một vệ tinh khối lượng $m = 500\\,\\text{kg}$ từ mặt đất ($R = 6.4 \\times 10^6\\,\\text{m}$) lên quỹ đạo có bán kính $r = 2R = 12.8 \\times 10^6\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính độ biến thiên thế năng hấp dẫn theo đơn vị Gigajun (GJ).",
            "unit": "GJ",
            "ans": 15.68,
            "tol": 0.1,
            "hints": ["$\\Delta U = U_2 - U_1 = -\\frac{GMm}{2R} - (-\\frac{GMm}{R}) = \\frac{GMm}{2R} = \\frac{mgR}{2}$.", "$1\\,\\text{GJ} = 10^9\\,\\text{J}$."],
            "solution": "$$\\Delta U = \\frac{500 \\times 9.8 \\times 6.4 \\times 10^6}{2} = 1.568 \\times 10^{10}\\,\\text{J} = 15.68\\,\\text{GJ}$$\\nĐáp số: 15.68 GJ"
        },
        {
            "id": "ex_6_7",
            "type": "mid",
            "q": "Sao Hỏa có bán trục lớn quỹ đạo quanh Mặt Trời là $a = 1.524\\,\\text{AU}$ (đơn vị thiên văn). Theo định luật Kepler III, chu kỳ quay của Sao Hỏa bằng bao nhiêu năm Trái Đất?",
            "unit": "năm",
            "ans": 1.88,
            "tol": 0.05,
            "hints": ["$T^2 = a^3 \\implies T = a^{1.5}$."],
            "solution": "$$T = (1.524)^{1.5} \\approx 1.8809 \\approx 1.88\\,\\text{năm}$$\\nĐáp số: 1.88 năm"
        },
        {
            "id": "ex_6_8",
            "type": "mid",
            "q": "Giả sử đào một đường hầm thẳng xuyên qua tâm Trái Đất ($R = 6.4 \\times 10^6\\,\\text{m}, g = 9.8\\,\\text{m/s}^2$). Thả một hòn bi rơi tự do vào hầm. Tính chu kỳ dao động của hòn bi theo phút.",
            "unit": "phút",
            "ans": 84.63,
            "tol": 0.2,
            "hints": ["Bi dao động điều hòa với $\\omega = \\sqrt{g/R}$.", "$T = 2\\pi\\sqrt{R/g}$, đổi sang phút."],
            "solution": "$$T = 2\\pi \\sqrt{\\frac{6.4 \\times 10^6}{9.8}} \\approx 5077.6\\,\\text{s} \\approx 84.63\\,\\text{phút}$$\\nĐáp số: 84.63 phút"
        },
        {
            "id": "ex_6_9",
            "type": "hard",
            "q": "Tàu vũ trụ bay trên elip quanh Trái Đất có cận địa $r_p = 6800\\,\\text{km}$ và viễn địa $r_a = 42200\\,\\text{km}$ ($a = 24500\\,\\text{km}$). $GM = 3.986 \\times 10^{14}\\,\\text{m}^3/\\text{s}^2$. Tính tốc độ của tàu tại cận địa (km/s).",
            "unit": "km/s",
            "ans": 10.05,
            "tol": 0.1,
            "hints": ["Phương trình vis-viva: $v_p^2 = GM(2/r_p - 1/a)$."],
            "solution": "$$v_p = \\sqrt{3.986 \\times 10^{14} \\times \\left(\\frac{2}{6.8 \\times 10^6} - \\frac{1}{2.45 \\times 10^7}\\right)} \\approx 10048\\,\\text{m/s} \\approx 10.05\\,\\text{km/s}$$\\nĐáp số: 10.05 km/s"
        },
        {
            "id": "ex_6_10",
            "type": "hard",
            "q": "Một vệ tinh địa tĩnh quay quanh Trái Đất với chu kỳ $T = 24\\,\\text{h} = 86400\\,\\text{s}$. Cho $GM = 3.986 \\times 10^{14}\\,\\text{m}^3/\\text{s}^2$. Hãy tính bán kính quỹ đạo của vệ tinh địa tĩnh theo đơn vị $10^6\\,\\text{m}$.",
            "unit": "×10⁶ m",
            "ans": 42.24,
            "tol": 0.2,
            "hints": ["$r = \\left(\\frac{GM T^2}{4\\pi^2}\\right)^{1/3}$."],
            "solution": "$$r = \\left(\\frac{3.986 \\times 10^{14} \\times 86400^2}{4\\pi^2}\\right)^{1/3} \\approx 4.2241 \\times 10^7\\,\\text{m} = 42.24 \\times 10^6\\,\\text{m}$$\\nĐáp số: 42.24"
        }
    ]
}

CH7 = {
    "id": 7,
    "num": 7,
    "part": "Phần I — Cơ học",
    "title": "Cơ học tương đối hẹp",
    "tag": "Biến đổi Lorentz & Động lực học tương đối tính",
    "status": "ready",
    "summary": "Hai tiên đề Einstein, phép biến đổi Lorentz, tính tương đối của sự đồng thời, co độ dài, giãn thời gian, công thức cộng vận tốc, hệ thức Einstein E = mc² và liên hệ năng lượng - xung lượng.",
    "nature": {
        "why": "Cơ học cổ điển Newton dựa trên thời gian và không gian tuyệt đối. Tuy nhiên, thí nghiệm Michelson - Morley và phương trình Maxwell chứng minh tốc độ ánh sáng trong chân không là bất biến, đòi hỏi phải tái định nghĩa cấu trúc không - thời gian.",
        "meaning": "Không gian và thời gian liên kết mật thiết thành thể liên tục 4 chiều Minkowski. Không có sự đồng thời tuyệt đối. Năng lượng và khối lượng là hai mặt của một thực thể qua hệ thức $E = mc^2$. Vật có khối lượng nghỉ không bao giờ đạt được tốc độ ánh sáng vì cần năng lượng vô hạn.",
        "conditions": "Áp dụng trong các hệ quy chiếu quán tính khi bỏ qua trường hấp dẫn (trọng trường yếu).",
        "limits": "Khi có gia tốc hoặc trường hấp dẫn mạnh, cấu trúc không thời gian bị bẻ cong, phải mở rộng sang Thuyết tương đối rộng."
    },
    "formulas": [
        {
            "name": "Phép biến đổi Lorentz và Thừa số γ",
            "latex": "x' = \\gamma(x - Vt); \\quad t' = \\gamma\\left(t - \\frac{Vx}{c^2}\\right); \\quad \\gamma = \\frac{1}{\\sqrt{1 - V^2/c^2}} \\ge 1",
            "meaning": "Chuyển đổi tọa độ và thời gian giữa hai hệ quán tính chuyển động tương đối vận tốc $V$. Khi $V \\ll c$, $\\gamma \\to 1$ quay về phép biến đổi Galilei.",
            "proof": [
                {"step": "x' = \\gamma(x - Vt), \\quad x = \\gamma(x' + Vt')", "reason": "Dạng tuyến tính đối xứng do tính đồng nhất của không-thời gian"},
                {"step": "x = ct \\implies x' = ct'", "reason": "Tiên đề 2 Einstein: Tốc độ ánh sáng c bất biến trong mọi hệ quán tính"},
                {"step": "c^2 t t' = \\gamma^2 (c - V)(c + V) t t' = \\gamma^2 (c^2 - V^2) t t'", "reason": "Nhân hai phương trình xung ánh sáng vế theo vế"},
                {"step": "\\gamma = \\frac{1}{\\sqrt{1 - V^2/c^2}}", "reason": "Rút gọn tt' và giải ra thừa số Lorentz"}
            ]
        },
        {
            "name": "Hiệu ứng Giãn thời gian, Co độ dài và Cộng vận tốc",
            "latex": "\\Delta t = \\gamma \\Delta t_0; \\quad L = \\frac{L_0}{\\gamma}; \\quad u_x = \\frac{u_x' + V}{1 + \\frac{u_x' V}{c^2}}",
            "meaning": "Đồng hồ chuyển động chạy chậm hơn đồng hồ đứng yên. Vật chuyển động bị co ngắn lại dọc theo chiều chuyển động. Vận tốc tổng hợp không bao giờ vượt quá $c$.",
            "proof": [
                {"step": "\\Delta t = t_2 - t_1 = \\gamma(t_2' - t_1') = \\gamma \\Delta t_0", "reason": "Khoảng thời gian riêng Δt₀ đo tại cùng một vị trí trong hệ riêng (Δx' = 0)"},
                {"step": "L_0 = x_2' - x_1' = \\gamma(x_2 - x_1) = \\gamma L \\implies L = L_0/\\gamma", "reason": "Đo chiều dài trong hệ đứng yên phải đo đồng thời hai đầu (Δt = 0)"},
                {"step": "u_x = \\frac{dx}{dt} = \\frac{\\gamma(dx' + V dt')}{\\gamma(dt' + \\frac{V}{c^2}dx')} = \\frac{u_x' + V}{1 + \\frac{u_x' V}{c^2}}", "reason": "Lấy vi phân biến đổi Lorentz và chia vế theo vế"}
            ]
        },
        {
            "name": "Động lượng, Năng lượng Tương đối tính và Hệ thức Einstein",
            "latex": "\\vec{p} = \\gamma m_0 \\vec{v}; \\quad E = \\gamma m_0 c^2; \\quad E^2 = p^2 c^2 + m_0^2 c^4; \\quad K = (\\gamma - 1)m_0 c^2",
            "meaning": "Khối lượng tương đương năng lượng. Khi $v \\ll c$: $K \\approx \\frac{1}{2}m_0 v^2 + \\frac{3}{8}m_0\\frac{v^4}{c^2}$.",
            "proof": [
                {"step": "dK = \\vec{F} \\cdot d\\vec{r} = v dp = v d(\\gamma m v)", "reason": "Định lý động năng với động lượng tương đối tính p = γ m v"},
                {"step": "K = \\int_0^p v dp = p v - \\int_0^v p dv", "reason": "Tích phân từng phần theo biến vận tốc v"},
                {"step": "K = \\gamma m v^2 + m c^2\\left(\\frac{1}{\\gamma} - 1\\right) = \\gamma m c^2 - m c^2 = (\\gamma - 1)m c^2", "reason": "Rút gọn đại số sử dụng đồng nhất thức γ²v² = γ²c² - c²"},
                {"step": "E^2 = (\\gamma m c^2)^2 = \\gamma^2 m^2 c^4 = p^2 c^2 + m^2 c^4", "reason": "Liên hệ năng lượng toàn phần và động lượng p"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Tính thừa số Lorentz, co độ dài và giãn thời gian",
            "algorithm": [
                "Bước 1: Tính $\\gamma = 1 / \\sqrt{1 - (v/c)^2}$.",
                "Bước 2: Xác định độ dài riêng $L_0$ và thời gian riêng $\\Delta t_0$ (đo trong hệ đứng yên cùng vật/đồng hồ).",
                "Bước 3: Áp dụng $L = L_0 / \\gamma$ (co ngắn) và $\\Delta t = \\gamma \\Delta t_0$ (chạy chậm).",
                "Bước 4: Kiểm tra: $L < L_0$ và $\\Delta t > \\Delta t_0$."
            ]
        },
        {
            "name": "Dạng 2: Năng lượng, động năng và xung lượng tương đối tính",
            "algorithm": [
                "Bước 1: Năng lượng nghỉ $E_0 = m_0 c^2$.",
                "Bước 2: Năng lượng toàn phần $E = \\gamma E_0 = K + E_0$.",
                "Bước 3: Sử dụng $E^2 = p^2 c^2 + E_0^2$ để tìm động lượng $p = \\frac{\\sqrt{E^2 - E_0^2}}{c}$.",
                "Bước 4: Tính tốc độ hạt: $v = \\frac{p c^2}{E} = c\\sqrt{1 - 1/\\gamma^2}$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Gia tốc electron đến động năng cao",
            "problem": "Một electron có năng lượng nghỉ $E_0 = m_0 c^2 = 0.511\\,\\text{MeV}$ được gia tốc đến động năng $K = 1.022\\,\\text{MeV} = 2 E_0$. Tính thừa số Lorentz $\\gamma$ và tốc độ của electron theo $c$.",
            "analysis": "Năng lượng toàn phần $E = K + E_0 = 3 E_0 \\implies \\gamma = 3$. Từ đó suy ra vận tốc.",
            "solution": "1. Thừa số Lorentz:\\n$$\\gamma = \\frac{E}{E_0} = \\frac{K + E_0}{E_0} = \\frac{2 E_0 + E_0}{E_0} = 3.0$$\\n2. Tốc độ của electron:\\n$$\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}} = 3 \\implies 1 - \\frac{v^2}{c^2} = \\frac{1}{9} \\implies \\frac{v^2}{c^2} = \\frac{8}{9}$$\\n$$v = c \\frac{\\sqrt{8}}{3} = c \\frac{2\\sqrt{2}}{3} \\approx 0.9428 c \\approx 0.943 c$$\\n(Nếu dùng cơ học Newton cổ điển $K = \\frac{1}{2}m v^2 \\implies v = \\sqrt{2K/m} = \\sqrt{4 c^2} = 2c > c$, hoàn toàn vô lý!)."
        }
    ],
    "pitfalls": [
        {
            "error": "Nhầm lẫn giữa hệ quy chiếu riêng và hệ quy chiếu quan sát",
            "fix": "Độ dài riêng $L_0$ chỉ đo khi vật đứng yên so với thước. Thời gian riêng $\\Delta t_0$ là thời gian giữa hai biến cố xảy ra tại cùng một vị trí trong hệ khảo sát.",
            "tip": "Đồng hồ riêng là đồng hồ gắn chặt vào người du hành; độ dài riêng là chiều dài đo khi đặt vật trên bàn trước mặt."
        }
    ],
    "exercises": [
        {
            "id": "ex_7_1",
            "type": "easy",
            "q": "Một hạt chuyển động với tốc độ $v = 0.6c$. Tính giá trị của thừa số Lorentz $\\gamma$.",
            "unit": "",
            "ans": 1.25,
            "tol": 0.01,
            "hints": ["$\\gamma = 1 / \\sqrt{1 - (v/c)^2} = 1 / \\sqrt{1 - 0.36}$."],
            "solution": "$$\\gamma = \\frac{1}{\\sqrt{1 - 0.36}} = \\frac{1}{\\sqrt{0.64}} = \\frac{1}{0.8} = 1.25$$\\nĐáp số: 1.25"
        },
        {
            "id": "ex_7_2",
            "type": "easy",
            "q": "Một con tàu vũ trụ có chiều dài riêng $L_0 = 100\\,\\text{m}$ bay qua Trái Đất với vận tốc $v = 0.8c$. Người quan sát trên Trái Đất đo được chiều dài của con tàu là bao nhiêu mét?",
            "unit": "m",
            "ans": 60.0,
            "tol": 0.1,
            "hints": ["$\\gamma = 1 / \\sqrt{1 - 0.64} = 1 / 0.6$.", "Chiều dài co ngắn $L = L_0 / \\gamma = L_0 \\sqrt{1 - 0.64}$."],
            "solution": "$$L = 100 \\times \\sqrt{1 - 0.8^2} = 100 \\times 0.6 = 60.0\\,\\text{m}$$\\nĐáp số: 60.0 m"
        },
        {
            "id": "ex_7_3",
            "type": "easy",
            "q": "Một phi hành gia trên tàu bay với vận tốc $v = 0.6c$ ($\gamma = 1.25$) đo được giấc ngủ của mình kéo dài $\\Delta t_0 = 10\\,\\text{s}$. Đồng hồ đặt trên Trái Đất ghi nhận khoảng thời gian này là bao nhiêu giây?",
            "unit": "s",
            "ans": 12.5,
            "tol": 0.1,
            "hints": ["$\\Delta t = \\gamma \\Delta t_0 = 1.25 \\times 10$."],
            "solution": "$$\\Delta t = 1.25 \\times 10 = 12.5\\,\\text{s}$$\\nĐáp số: 12.5 s"
        },
        {
            "id": "ex_7_4",
            "type": "easy",
            "q": "Tính năng lượng nghỉ chứa trong $m_0 = 1.0\\,\\text{kg}$ vật chất theo đơn vị $10^{16}\\,\\text{J}$ (lấy $c = 3.0 \\times 10^8\\,\\text{m/s}$).",
            "unit": "×10¹⁶ J",
            "ans": 9.0,
            "tol": 0.05,
            "hints": ["$E_0 = m_0 c^2 = 1.0 \\times (3.0 \\times 10^8)^2$."],
            "solution": "$$E_0 = 1.0 \\times 9.0 \\times 10^{16} = 9.0 \\times 10^{16}\\,\\text{J}$$\\nĐáp số: 9.0"
        },
        {
            "id": "ex_7_5",
            "type": "mid",
            "q": "Hai hạt bay đối đầu nhau đối với phòng thí nghiệm, mỗi hạt có tốc độ $0.8c$. Tính vận tốc tương đối giữa hai hạt theo phân số của $c$ (làm tròn 2 chữ số).",
            "unit": "c",
            "ans": 0.98,
            "tol": 0.02,
            "hints": ["Công thức cộng vận tốc: $u = \\frac{v_1 + v_2}{1 + v_1 v_2 / c^2}$."],
            "solution": "$$u = \\frac{0.8 + 0.8}{1 + 0.64} = \\frac{1.6}{1.64} \\approx 0.9756c \\approx 0.98c$$\\nĐáp số: 0.98 c"
        },
        {
            "id": "ex_7_6",
            "type": "mid",
            "q": "Hạt muon có thời gian sống riêng $\\tau_0 = 2.2\\,\\mu\\text{s} = 2.2 \\times 10^{-6}\\,\\text{s}$ chuyển động trong khí quyển với tốc độ $v = 0.98c$ ($c = 3 \\times 10^8\\,\\text{m/s}$). Quãng đường hạt bay được quan sát từ mặt đất là bao nhiêu km?",
            "unit": "km",
            "ans": 3.25,
            "tol": 0.1,
            "hints": ["$\\gamma = 1 / \\sqrt{1 - 0.98^2} \\approx 5.025$.", "$d = v \\gamma \\tau_0$."],
            "solution": "$$\\gamma = \\frac{1}{\\sqrt{1 - 0.9604}} = \\frac{1}{\\sqrt{0.0396}} \\approx 5.025$$\\n$$d = 0.98 \\times (3 \\times 10^8) \\times 5.025 \\times (2.2 \\times 10^{-6}) \\approx 3250\\,\\text{m} = 3.25\\,\\text{km}$$\\nĐáp số: 3.25 km"
        },
        {
            "id": "ex_7_7",
            "type": "mid",
            "q": "Một electron ($E_0 = 0.511\\,\\text{MeV}$) chuyển động với vận tốc $v = 0.8c$. Tính động năng tương đối tính $K$ của electron theo MeV (làm tròn 3 chữ số).",
            "unit": "MeV",
            "ans": 0.341,
            "tol": 0.01,
            "hints": ["$\\gamma = 1 / \\sqrt{1 - 0.64} = 1.6667$.", "$K = (\\gamma - 1) E_0$."],
            "solution": "$$K = (1.6667 - 1) \\times 0.511 = 0.6667 \\times 0.511 \\approx 0.3407 \\approx 0.341\\,\\text{MeV}$$\\nĐáp số: 0.341 MeV"
        },
        {
            "id": "ex_7_8",
            "type": "mid",
            "q": "Một proton có năng lượng toàn phần $E = 2.0\\,\\text{GeV}$ và năng lượng nghỉ $E_0 = 0.938\\,\\text{GeV}$. Tính động lượng $p$ của proton theo đơn vị $\\text{GeV}/c$.",
            "unit": "GeV/c",
            "ans": 1.77,
            "tol": 0.05,
            "hints": ["$p c = \\sqrt{E^2 - E_0^2}$."],
            "solution": "$$p = \\sqrt{2.0^2 - 0.938^2} = \\sqrt{4.0 - 0.8798} = \\sqrt{3.1202} \\approx 1.766 \\approx 1.77\\,\\text{GeV}/c$$\\nĐáp số: 1.77 GeV/c"
        },
        {
            "id": "ex_7_9",
            "type": "hard",
            "q": "Một thiên hà đang lùi xa Trái Đất với tốc độ $V = 0.6c$. Một vạch quang phổ có bước sóng riêng phát xạ $\\lambda_0 = 500\\,\\text{nm}$. Tính bước sóng $\\lambda$ thu được trên Trái Đất theo nm.",
            "unit": "nm",
            "ans": 1000.0,
            "tol": 1.0,
            "hints": ["Công thức Doppler dịch đỏ: $\\lambda = \\lambda_0 \\sqrt{\\frac{1 + \\beta}{1 - \\beta}}$ với $\\beta = 0.6$."],
            "solution": "$$\\lambda = 500 \\times \\sqrt{\\frac{1 + 0.6}{1 - 0.6}} = 500 \\times \\sqrt{\\frac{1.6}{0.4}} = 500 \\times \\sqrt{4} = 1000.0\\,\\text{nm}$$\\nĐáp số: 1000.0 nm"
        },
        {
            "id": "ex_7_10",
            "type": "hard",
            "q": "Một hạt có động năng bằng hai lần năng lượng nghỉ ($K = 2 m_0 c^2$). Tính vận tốc của hạt theo tỉ số $v/c$ (làm tròn 3 chữ số).",
            "unit": "v/c",
            "ans": 0.943,
            "tol": 0.01,
            "hints": ["$\\gamma - 1 = 2 \\implies \\gamma = 3$.", "$v/c = \\sqrt{1 - 1/\\gamma^2} = \\sqrt{8}/3$."],
            "solution": "$$\\frac{v}{c} = \\sqrt{1 - \\frac{1}{9}} = \\frac{\\sqrt{8}}{3} \\approx 0.9428 \\approx 0.943$$\\nĐáp số: 0.943"
        }
    ]
}

CH8 = {
    "id": 8,
    "num": 8,
    "part": "Phần I — Cơ học",
    "title": "Cơ học chất lưu",
    "tag": "Pascal, Bernoulli & Độ nhớt Poiseuille",
    "status": "ready",
    "summary": "Áp suất thủy tĩnh, nguyên lý Pascal, lực đẩy Archimedes, phương trình liên tục, phương trình Bernoulli cho chất lưu lý tưởng, chất lưu nhớt (định luật Poiseuille), hiện tượng bề mặt và mao dẫn.",
    "nature": {
        "why": "Chất lưu (chất lỏng và chất khí) không giữ hình dạng cố định mà có thể chảy dưới tác dụng của ứng suất tiếp, đòi hỏi phương pháp mô tả trường vận tốc và áp suất liên tục.",
        "meaning": "Phương trình Bernoulli là biểu hiện của định luật bảo toàn cơ năng trên một đường dòng chất lưu lý tưởng. Ở nơi dòng chảy nhanh, áp suất tĩnh giảm. Lực cản nội ma sát xuất hiện do sự trượt tương đối giữa các lớp chất lưu.",
        "conditions": "Phương trình Bernoulli chuẩn áp dụng cho chất lưu lý tưởng: Ổn định, không nén được, không nhớt và không xoáy.",
        "limits": "Khi chảy rối ($Re > Re_{th}$) hoặc chất lỏng có độ nhớt lớn, năng lượng cơ học hao tán thành nhiệt theo định luật Poiseuille."
    },
    "formulas": [
        {
            "name": "Phương trình Thủy tĩnh học và Nguyên lý Pascal",
            "latex": "p = p_0 + \\rho gh; \\quad \\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\frac{A_2}{A_1}",
            "meaning": "Áp suất thủy tĩnh tăng tuyến tính theo độ sâu. Độ tăng áp suất tác dụng lên chất lỏng kín được truyền nguyên vẹn theo mọi hướng.",
            "proof": [
                {"step": "p(z)A - p(z + dz)A - \\rho g A dz = 0", "reason": "Điều kiện cân bằng tĩnh của phần tử chất lỏng hình trụ diện tích A, chiều cao dz"},
                {"step": "-dp = \\rho g dz \\implies p = p_0 + \\rho gh", "reason": "Tích phân theo chiều sâu h = -z"}
            ]
        },
        {
            "name": "Phương trình liên tục và Định luật Bernoulli",
            "latex": "A_1 v_1 = A_2 v_2 = Q = \\text{const}; \\quad p + \\frac{1}{2}\\rho v^2 + \\rho gh = \\text{const}",
            "meaning": "Bảo toàn khối lượng và bảo toàn cơ năng trên đường dòng. Ba số hạng là áp suất tĩnh, áp suất động và áp suất thế.",
            "proof": [
                {"step": "\\Delta m_1 = \\rho A_1 v_1 dt = \\rho A_2 v_2 dt = \\Delta m_2", "reason": "Chất lỏng không nén được, khối lượng vào bằng khối lượng ra"},
                {"step": "(p_1 - p_2)\\Delta V = \\frac{1}{2}\\rho \\Delta V(v_2^2 - v_1^2) + \\rho \\Delta V g(h_2 - h_1)", "reason": "Công của lực áp suất bằng độ biến thiên động năng cộng độ biến thiên thế năng"},
                {"step": "p_1 + \\frac{1}{2}\\rho v_1^2 + \\rho gh_1 = p_2 + \\frac{1}{2}\\rho v_2^2 + \\rho gh_2", "reason": "Chia hai vế cho thể tích ΔV và chuyển vế"}
            ]
        },
        {
            "name": "Chất lưu nhớt (Poiseuille) và Mao dẫn (Laplace)",
            "latex": "Q = \\frac{\\pi R^4 \\Delta p}{8\\eta L}; \\quad \\Delta p_{Laplace} = \\frac{2\\sigma}{R}; \\quad h_{mao\\,dan} = \\frac{2\\sigma\\cos\\theta}{\\rho g r}",
            "meaning": "Lưu lượng chảy tầng trong ống tròn tỉ lệ với lũy thừa bậc 4 của bán kính $R^4$. Lực căng bề mặt kéo cột chất lỏng dâng lên trong ống mao dẫn.",
            "proof": [
                {"step": "F_{nhot} = -\\eta (2\\pi r L)\\frac{dv}{dr} = \\Delta p (\\pi r^2)", "reason": "Cân bằng lực giữa áp lực đẩy và lực ma sát nhớt trên mặt trụ bán kính r"},
                {"step": "v(r) = \\frac{\\Delta p}{4\\eta L}(R^2 - r^2) \\implies Q = \\int_0^R v(r) 2\\pi r dr = \\frac{\\pi R^4 \\Delta p}{8\\eta L}", "reason": "Tích phân phân bố vận tốc dạng parabol thu được công thức Poiseuille"},
                {"step": "2\\pi r \\sigma \\cos\\theta = m g = \\rho (\\pi r^2 h) g \\implies h = \\frac{2\\sigma\\cos\\theta}{\\rho g r}", "reason": "Cân bằng giữa lực căng bề mặt hướng lên và trọng lượng cột chất lỏng"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Áp suất thủy tĩnh, lực đẩy Archimedes và lực lên thành đập",
            "algorithm": [
                "Bước 1: Áp suất ở độ sâu $h$: $p = p_0 + \\rho gh$.",
                "Bước 2: Lực đẩy Archimedes: $F_A = \\rho_{lu} V_{chìm} g$. Điều kiện nổi: $V_{chìm} = V \\frac{\\rho_{vật}}{\\rho_{lu}}$.",
                "Bước 3: Tổng áp lực lên mặt đập đứng rộng $w$, sâu $H$: $F = \\frac{1}{2}\\rho g w H^2$ (đặt tại độ sâu $2H/3$).",
                "Bước 4: Kiểm tra thứ nguyên lực [N] và áp suất [Pa]."
            ]
        },
        {
            "name": "Dạng 2: Ứng dụng phương trình Bernoulli (Ống Venturi, Torricelli, Pitot)",
            "algorithm": [
                "Bước 1: Áp dụng phương trình liên tục $v_2 = v_1 \\frac{A_1}{A_2}$.",
                "Bước 2: Áp dụng phương trình Bernoulli giữa hai điểm: $p_1 + \\frac{1}{2}\\rho v_1^2 = p_2 + \\frac{1}{2}\\rho v_2^2$.",
                "Bước 3: Tính độ chênh áp suất $\\Delta p = \\frac{1}{2}\\rho(v_2^2 - v_1^2)$ hoặc lưu lượng $Q = A_1 v_1$.",
                "Bước 4: Kiểm tra giới hạn: Tiết diện nhỏ $\\implies$ vận tốc lớn $\\implies$ áp suất tĩnh giảm."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Đo lưu lượng bằng ống Venturi",
            "problem": "Nước chảy trong ống Venturi nằm ngang. Tiết diện ống rộng $A_1 = 100\\,\\text{cm}^2$, chỗ thắt $A_2 = 25\\,\\text{cm}^2$. Áp kế đo được độ chênh áp suất giữa hai phần là $\\Delta p = 7.5\\,\\text{kPa} = 7500\\,\\text{Pa}$. Cho $\\rho_{nuoc} = 1000\\,\\text{kg/m}^3$. Tính lưu lượng dòng chảy $Q$ theo lít/giây.",
            "analysis": "Từ phương trình liên tục: $v_2 = v_1(A_1/A_2) = 4v_1$. Thay vào Bernoulli để tính $v_1$, sau đó tính $Q = A_1 v_1$.",
            "solution": "1. Liên hệ vận tốc: $v_2 = 4 v_1 \\implies v_2^2 = 16 v_1^2$.\\n2. Theo Bernoulli nằm ngang:\\n$$\\Delta p = p_1 - p_2 = \\frac{1}{2}\\rho (v_2^2 - v_1^2) = \\frac{1}{2}(1000)(15 v_1^2) = 7500 v_1^2$$\\n$$7500 = 7500 v_1^2 \\implies v_1 = 1.0\\,\\text{m/s}$$\\n3. Lưu lượng chảy:\\n$$Q = A_1 v_1 = (100 \\times 10^{-4}\\,\\text{m}^2) \\times 1.0\\,\\text{m/s} = 0.01\\,\\text{m}^3/\\text{s} = 10.0\\,\\text{lít/giây}$$\\nĐáp số: 10.0 lít/giây."
        }
    ],
    "pitfalls": [
        {
            "error": "Áp dụng phương trình Bernoulli cho dòng chảy có ma sát lớn hoặc chảy rối",
            "fix": "Bernoulli chỉ áp dụng cho dòng chảy tầng của chất lưu lý tưởng. Khi có độ nhớt lớn, phải sử dụng định luật Poiseuille kèm theo sụt áp dọc đường ống.",
            "tip": "Đoạn ống hẹp dài có độ nhớt $\\to$ Poiseuille ($Q \\propto R^4$); chỗ thắt cục bộ ngắn $\\to$ Bernoulli."
        }
    ],
    "exercises": [
        {
            "id": "ex_8_1",
            "type": "easy",
            "q": "Tại độ sâu $h = 25\\,\\text{m}$ dưới mặt nước hồ ($\rho = 1000\\,\\text{kg/m}^3, g = 9.8\\,\\text{m/s}^2$). Cho áp suất khí quyển $p_0 = 101.3\\,\\text{kPa}$. Tính áp suất tuyệt đối tại điểm đó theo kPa.",
            "unit": "kPa",
            "ans": 346.3,
            "tol": 0.5,
            "hints": ["$p = p_0 + \\rho gh$."],
            "solution": "$$p = 101.3 + \\frac{1000 \\times 9.8 \\times 25}{1000} = 101.3 + 245.0 = 346.3\\,\\text{kPa}$$\\nĐáp số: 346.3 kPa"
        },
        {
            "id": "ex_8_2",
            "type": "easy",
            "q": "Một máy ép thủy lực có tiết diện hai piston lần lượt là $A_1 = 10\\,\\text{cm}^2$ và $A_2 = 250\\,\\text{cm}^2$. Tác dụng lực $F_1 = 120\\,\\text{N}$ lên piston nhỏ. Lực nâng $F_2$ tác dụng lên piston lớn là bao nhiêu Newton?",
            "unit": "N",
            "ans": 3000.0,
            "tol": 1.0,
            "hints": ["$F_2 = F_1 \\frac{A_2}{A_1}$."],
            "solution": "$$F_2 = 120 \\times \\frac{250}{10} = 120 \\times 25 = 3000.0\\,\\text{N}$$\\nĐáp số: 3000.0 N"
        },
        {
            "id": "ex_8_3",
            "type": "easy",
            "q": "Nước chảy trong ống ngang có tiết diện $A_1 = 20\\,\\text{cm}^2$ với vận tốc $v_1 = 1.5\\,\\text{m/s}$. Tại chỗ thắt có tiết diện $A_2 = 5\\,\\text{cm}^2$, tốc độ nước chảy $v_2$ là bao nhiêu m/s?",
            "unit": "m/s",
            "ans": 6.0,
            "tol": 0.05,
            "hints": ["Phương trình liên tục: $A_1 v_1 = A_2 v_2$."],
            "solution": "$$v_2 = 1.5 \\times \\frac{20}{5} = 1.5 \\times 4 = 6.0\\,\\text{m/s}$$\\nĐáp số: 6.0 m/s"
        },
        {
            "id": "ex_8_4",
            "type": "easy",
            "q": "Một thùng nước hở có lỗ rò nhỏ ở đáy cách mặt thoáng nước một khoảng $h = 3.2\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính tốc độ nước phụt ra từ lỗ rò theo công thức Torricelli (m/s).",
            "unit": "m/s",
            "ans": 7.92,
            "tol": 0.05,
            "hints": ["$v = \\sqrt{2gh}$."],
            "solution": "$$v = \\sqrt{2 \\times 9.8 \\times 3.2} = \\sqrt{62.72} \\approx 7.9196 \\approx 7.92\\,\\text{m/s}$$\\nĐáp số: 7.92 m/s"
        },
        {
            "id": "ex_8_5",
            "type": "mid",
            "q": "Một tảng băng ($\rho_{b} = 917\\,\\text{kg/m}^3$) nổi trên nước biển ($\rho_{n} = 1025\\,\\text{kg/m}^3$). Tính phần trăm thể tích của tảng băng bị chìm dưới mặt nước (làm tròn 1 chữ số thập phân).",
            "unit": "%",
            "ans": 89.5,
            "tol": 0.2,
            "hints": ["$V_c / V = \\rho_b / \\rho_n$."],
            "solution": "$$\\frac{V_c}{V} = \\frac{917}{1025} \\times 100\\% \\approx 89.463\\% \\approx 89.5\\%$$\\nĐáp số: 89.5 %"
        },
        {
            "id": "ex_8_6",
            "type": "mid",
            "q": "Nước ($\rho = 1000\\,\\text{kg/m}^3$) chảy trong ống ngang từ tiết diện $A_1$ sang $A_2 = A_1 / 3$. Vận tốc tại tiết diện 1 là $v_1 = 2\\,\\text{m/s}$. Tính độ chênh lệch áp suất tĩnh $\\Delta p = p_1 - p_2$ theo đơn vị kPa.",
            "unit": "kPa",
            "ans": 16.0,
            "tol": 0.1,
            "hints": ["$v_2 = 3v_1 = 6\\,\\text{m/s}$.", "$\\Delta p = \\frac{1}{2}\\rho (v_2^2 - v_1^2)$."],
            "solution": "$$\\Delta p = \\frac{1}{2} \\times 1000 \\times (6^2 - 2^2) = 500 \\times 32 = 16000\\,\\text{Pa} = 16.0\\,\\text{kPa}$$\\nĐáp số: 16.0 kPa"
        },
        {
            "id": "ex_8_7",
            "type": "mid",
            "q": "Một đập chắn nước thẳng đứng có bề rộng $w = 20\\,\\text{m}$, nước sâu $H = 6\\,\\text{m}$ ($\rho = 1000\\,\\text{kg/m}^3, g = 9.8\\,\\text{m/s}^2$). Tính tổng áp lực thủy tĩnh của nước lên mặt đập theo đơn vị Meganewton (MN).",
            "unit": "MN",
            "ans": 3.53,
            "tol": 0.05,
            "hints": ["$F = \\frac{1}{2}\\rho g w H^2$.", "$1\\,\\text{MN} = 10^6\\,\\text{N}$."],
            "solution": "$$F = \\frac{1}{2} \\times 1000 \\times 9.8 \\times 20 \\times 6^2 = 98000 \\times 36 = 3528000\\,\\text{N} \\approx 3.53\\,\\text{MN}$$\\nĐáp số: 3.53 MN"
        },
        {
            "id": "ex_8_8",
            "type": "mid",
            "q": "Một ống mao dẫn bán kính trong $r = 0.5\\,\\text{mm} = 5 \\times 10^{-4}\\,\\text{m}$ nhúng thẳng đứng vào nước ($\rho = 1000\\,\\text{kg/m}^3, \\sigma = 0.073\\,\\text{N/m}, \\theta = 0^\\circ, g = 9.8\\,\\text{m/s}^2$). Độ dâng của cột nước trong ống là bao nhiêu mm?",
            "unit": "mm",
            "ans": 29.8,
            "tol": 0.2,
            "hints": ["$h = \\frac{2\\sigma\\cos\\theta}{\\rho g r}$."],
            "solution": "$$h = \\frac{2 \\times 0.073 \\times 1}{1000 \\times 9.8 \\times 5 \\times 10^{-4}} = \\frac{0.146}{4.9} \\approx 0.0298\\,\\text{m} = 29.8\\,\\text{mm}$$\\nĐáp số: 29.8 mm"
        },
        {
            "id": "ex_8_9",
            "type": "hard",
            "q": "Do bệnh xơ vữa, bán kính lòng động mạch giảm đi $20\\%$ ($R' = 0.8R$). Theo định luật Poiseuille, nếu giữ nguyên hiệu áp $\\Delta p$, lưu lượng máu $Q'$ sẽ bị giảm đi bao nhiêu phần trăm?",
            "unit": "%",
            "ans": 59.0,
            "tol": 0.5,
            "hints": ["$Q \\propto R^4$.", "$\\frac{Q'}{Q} = (0.8)^4 = 0.4096 \\implies \\%\\,\\text{giảm} = (1 - 0.4096) \\times 100\\%$."],
            "solution": "$$\\%\\,\\text{giảm} = (1 - 0.8^4) \\times 100\\% = (1 - 0.4096) \\times 100\\% = 59.04\\% \\approx 59.0\\%$$\\nĐáp số: 59.0 %"
        },
        {
            "id": "ex_8_10",
            "type": "hard",
            "q": "Một giọt nước mưa hình cầu bán kính $r = 2 \\times 10^{-5}\\,\\text{m}$ rơi trong không khí ($\eta = 1.8 \\times 10^{-5}\\,\\text{Pa}\\cdot\\text{s}, \\rho = 1000\\,\\text{kg/m}^3, g = 9.8\\,\\text{m/s}^2$). Tính vận tốc rơi tới hạn $v_\\infty$ của giọt mưa theo đơn vị cm/s.",
            "unit": "cm/s",
            "ans": 4.84,
            "tol": 0.1,
            "hints": ["Công thức Stokes: $v_\\infty = \\frac{2 r^2 \\rho g}{9\\eta}$. Đổi m/s ra cm/s."],
            "solution": "$$v_\\infty = \\frac{2 \\times (2 \\times 10^{-5})^2 \\times 1000 \\times 9.8}{9 \\times 1.8 \\times 10^{-5}} = \\frac{7.84 \\times 10^{-6}}{1.62 \\times 10^{-4}} \\approx 0.048395\\,\\text{m/s} \\approx 4.84\\,\\text{cm/s}$$\\nĐáp số: 4.84 cm/s"
        }
    ]
}

print("Chapters 6, 7, 8 data module ready.")
