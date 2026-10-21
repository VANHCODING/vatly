# -*- coding: utf-8 -*-
"""
Module defining data for Chapter 9 (Dao động cơ) and Chapter 10 (Sóng cơ)
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

CH9 = {
    "id": 9,
    "num": 9,
    "part": "Phần II — Dao động và Sóng cơ",
    "title": "Dao động cơ",
    "tag": "Điều hòa, Tắt dần & Cộng hưởng",
    "status": "ready",
    "summary": "Dao động điều hòa, con lắc lò xo, con lắc đơn, con lắc vật lý, năng lượng dao động, tổng hợp dao động cùng phương và vuông góc (Lissajous), dao động tắt dần, dao động cưỡng bức và cộng hưởng.",
    "nature": {
        "why": "Dao động là chuyển động phổ biến nhất trong tự nhiên: Mọi hệ cân bằng bền khi bị kích thích nhẹ đều thực hiện dao động quanh vị trí cân bằng do lực hồi phục kéo về.",
        "meaning": "Dao động điều hòa là hình chiếu của chuyển động tròn đều lên một trục. Tần số góc $\\omega_0$ chỉ phụ thuộc đặc tính cấu trúc hệ (tính đẳng thời: chu kỳ không phụ thuộc biên độ). Lực cản làm tiêu hao cơ năng tạo nên dao động tắt dần. Khi có ngoại lực biến thiên điều hòa kích thích, hệ chuyển sang dao động cưỡng bức; khi tần số ngoại lực xấp xỉ tần số riêng, biên độ vọt lên cực đại sinh ra hiện tượng Cộng hưởng.",
        "conditions": "Dao động điều hòa đòi hỏi góc lệch nhỏ ($\\sin\\theta \\approx \\theta$) hoặc lực hồi phục tuân theo định luật Hooke $F = -kx$.",
        "limits": "Khi biên độ lớn, xuất hiện tính phi tuyến (chu kỳ phụ thuộc biên độ). Khi ma sát quá lớn ($\\gamma \\ge \\omega_0$), hệ mất khả năng dao động và chuyển sang chế độ quá cản."
    },
    "formulas": [
        {
            "name": "Phương trình Vi phân và Nghiệm của Dao động điều hòa",
            "latex": "\\ddot{x} + \\omega_0^2 x = 0; \\quad x(t) = A\\cos(\\omega_0 t + \\varphi); \\quad A^2 = x^2 + \\frac{v^2}{\\omega_0^2}; \\quad E = \\frac{1}{2}m\\omega_0^2 A^2",
            "meaning": "Gia tốc luôn tỉ lệ và ngược pha với li độ: $a = -\\omega_0^2 x$. Vận tốc sớm pha $\\pi/2$ so với li độ. Cơ năng bảo toàn và tỉ lệ với bình phương biên độ $A^2$.",
            "proof": [
                {"step": "m\\ddot{x} = -kx \\implies \\ddot{x} + \\frac{k}{m}x = 0", "reason": "Định luật II Newton với lực hồi phục đàn hồi Hooke"},
                {"step": "\\omega_0 = \\sqrt{\\frac{k}{m}} \\implies \\ddot{x} + \\omega_0^2 x = 0", "reason": "Đặt tần số góc riêng ω₀"},
                {"step": "x(t) = C_1\\cos\\omega_0 t + C_2\\sin\\omega_0 t = A\\cos(\\omega_0 t + \\varphi)", "reason": "Nghiệm tổng quát của phương trình vi phân tuyến tính thuần nhất bậc hai"},
                {"step": "v(t) = \\dot{x} = -A\\omega_0\\sin(\\omega_0 t + \\varphi)", "reason": "Lấy đạo hàm bậc nhất theo thời gian"},
                {"step": "\\cos^2(\\omega_0 t + \\varphi) + \\sin^2(\\omega_0 t + \\varphi) = \\left(\\frac{x}{A}\\right)^2 + \\left(\\frac{v}{A\\omega_0}\\right)^2 = 1", "reason": "Đồng nhất thức lượng giác suy ra hệ thức độc lập với thời gian"}
            ]
        },
        {
            "name": "Các Hệ dao động tiêu biểu (Con lắc đơn, Con lắc vật lý)",
            "latex": "T_{lò\\,xo} = 2\\pi\\sqrt{\\frac{m}{k}}; \\quad T_{đơn} = 2\\pi\\sqrt{\\frac{\\ell}{g}}; \\quad T_{vật\\,lý} = 2\\pi\\sqrt{\\frac{I}{mgd}} = 2\\pi\\sqrt{\\frac{\\ell_0}{g}}",
            "meaning": "Con lắc vật lý quay quanh trục ngang cách khối tâm đoạn $d$ có chu kỳ tương đương con lắc đơn chiều dài quy đổi $\\ell_0 = I/(md)$.",
            "proof": [
                {"step": "I \\ddot{\\theta} = -mgd\\sin\\theta \\approx -mgd\\theta", "reason": "Phương trình quay quanh trục cố định với góc lệch nhỏ sinθ ≈ θ"},
                {"step": "\\ddot{\\theta} + \\frac{mgd}{I}\\theta = 0 \\implies \\omega_0 = \\sqrt{\\frac{mgd}{I}}", "reason": "Đưa về dạng phương trình vi phân dao động điều hòa"},
                {"step": "T = \\frac{2\\pi}{\\omega_0} = 2\\pi\\sqrt{\\frac{I}{mgd}}", "reason": "Công thức chu kỳ dao động con lắc vật lý"}
            ]
        },
        {
            "name": "Dao động Tắt dần, Cưỡng bức và Hiện tượng Cộng hưởng",
            "latex": "\\ddot{x} + 2\\gamma\\dot{x} + \\omega_0^2 x = \\frac{F_0}{m}\\cos\\Omega t; \\quad A(\\Omega) = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\Omega^2)^2 + 4\\gamma^2 \\Omega^2}}; \\quad \\Omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2}",
            "meaning": "Khi tần số ngoại lực $\\Omega$ tiến sát $\\Omega_r$, biên độ đạt cực đại $A_{\\max} \\approx \\frac{F_0}{2m\\gamma\\omega_0} = Q\\frac{F_0}{k}$. $Q = \\omega_0/(2\\gamma)$ là hệ số phẩm chất.",
            "proof": [
                {"step": "x(t) = \\text{Re}(\\hat{A}e^{i\\Omega t})", "reason": "Phương pháp biên độ phức trong dao động điều hòa"},
                {"step": "\\hat{A}(-\\Omega^2 + 2i\\gamma\\Omega + \\omega_0^2) = f_0 \\implies \\hat{A} = \\frac{f_0}{(\\omega_0^2 - \\Omega^2) + 2i\\gamma\\Omega}", "reason": "Thế nghiệm phức vào phương trình vi phân"},
                {"step": "A(\\Omega) = |\\hat{A}| = \\frac{f_0}{\\sqrt{(\\omega_0^2 - \\Omega^2)^2 + 4\\gamma^2 \\Omega^2}}", "reason": "Lấy môđun số phức để tìm biên độ dao động dừng"},
                {"step": "\\frac{d}{d(\\Omega^2)}[(\\omega_0^2 - \\Omega^2)^2 + 4\\gamma^2 \\Omega^2] = 0 \\implies \\Omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2}", "reason": "Cực đại biên độ đạt được khi mẫu số đạt cực tiểu"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Viết phương trình dao động, tính đại lượng thời gian và độc lập",
            "algorithm": [
                "Bước 1: Tính tần số góc $\\omega_0 = \\sqrt{k/m}$ hoặc $\\sqrt{g/\\ell}$.",
                "Bước 2: Sử dụng điều kiện ban đầu ($x_0, v_0$) để tìm biên độ $A = \\sqrt{x_0^2 + v_0^2/\\omega_0^2}$ và pha ban đầu $\\tan\\varphi = -v_0/(\\omega_0 x_0)$.",
                "Bước 3: Tính năng lượng: $E = \\frac{1}{2}kA^2$, động năng $K = \\frac{1}{2}mv^2$, thế năng $U = \\frac{1}{2}kx^2$.",
                "Bước 4: Kiểm tra: Tại biên $x = \\pm A \\implies v = 0, U = E$; tại cân bằng $x = 0 \\implies |v| = v_{\\max}, K = E$."
            ]
        },
        {
            "name": "Dạng 2: Tổng hợp dao động (Cùng tần số, phách và hình Lissajous)",
            "algorithm": [
                "Bước 1: Cùng phương cùng tần số: Dùng giản đồ Fresnel hoặc số phức $A_1\\angle\\varphi_1 + A_2\\angle\\varphi_2$. Biên độ tổng: $A^2 = A_1^2 + A_2^2 + 2A_1 A_2 \\cos(\\varphi_2 - \\varphi_1)$.",
                "Bước 2: Cùng phương khác tần số gần nhau ($\\\\omega_1 \\approx \\omega_2$): Hiện tượng phách với tần số phách $f_{ph} = |f_1 - f_2|$.",
                "Bước 3: Vuông góc cùng tần số: Khử $t$ suy ra phương trình elip $\\frac{x^2}{A^2} + \\frac{y^2}{B^2} - \\frac{2xy}{AB}\\cos\\Delta\\varphi = \\sin^2\\Delta\\varphi$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Khảo sát dao động con lắc lò xo",
            "problem": "Một con lắc lò xo gồm vật nặng $m = 0.4\\,\\text{kg}$, lò xo có độ cứng $k = 40\\,\\text{N/m}$. Kéo vật lệch khỏi vị trí cân bằng một đoạn $x_0 = 3\\,\\text{cm}$ rồi truyền cho nó vận tốc $v_0 = 40\\,\\text{cm/s} = 0.4\\,\\text{m/s}$ hướng ra xa vị trí cân bằng. Tính chu kỳ $T$, biên độ dao động $A$ và cơ năng $E$.",
            "analysis": "Tính $\\omega_0 = \\sqrt{k/m}$, sau đó dùng công thức độc lập thời gian để tìm $A$ và cơ năng $E = \\frac{1}{2}kA^2$.",
            "solution": "1. Tần số góc và chu kỳ:\\n$$\\omega_0 = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{40}{0.4}} = \\sqrt{100} = 10\\,\\text{rad/s}$$\\n$$T = \\frac{2\\pi}{\\omega_0} = \\frac{2\\pi}{10} \\approx 0.628\\,\\text{s}$$\\n2. Biên độ dao động:\\n$$A = \\sqrt{x_0^2 + \\frac{v_0^2}{\\omega_0^2}} = \\sqrt{0.03^2 + \\frac{0.4^2}{10^2}} = \\sqrt{0.0009 + 0.0016} = \\sqrt{0.0025} = 0.05\\,\\text{m} = 5.0\\,\\text{cm}$$\\n3. Cơ năng toàn phần:\\n$$E = \\frac{1}{2}k A^2 = \\frac{1}{2}(40)(0.05)^2 = 20 \\times 0.0025 = 0.05\\,\\text{J}$$\\nĐáp số: T = 0.628 s; A = 5.0 cm; E = 0.05 J."
        }
    ],
    "pitfalls": [
        {
            "error": "Quên rằng chu kỳ con lắc đơn tăng lên khi biên độ góc lớn (θ > 10°)",
            "fix": "Công thức $T = 2\\pi\\sqrt{\\ell/g}$ chỉ là gần đúng bậc nhất khi góc nhỏ $\\sin\\theta \\approx \\theta$. Khi góc lệch lớn, $T = T_0(1 + \\frac{\\theta_0^2}{16} + \\dots) > T_0$.",
            "tip": "Chỉ áp dụng tính đẳng thời của con lắc đơn khi góc lệch cực đại $\\alpha_0 \\le 10^\\circ$."
        }
    ],
    "exercises": [
        {
            "id": "ex_9_1",
            "type": "easy",
            "q": "Một con lắc lò xo có $m = 0.4\\,\\text{kg}$ gắn với lò xo độ cứng $k = 40\\,\\text{N/m}$. Tính chu kỳ dao động riêng $T$ của con lắc theo giây (làm tròn 3 chữ số thập phân).",
            "unit": "s",
            "ans": 0.628,
            "tol": 0.01,
            "hints": ["$T = 2\\pi \\sqrt{m/k}$."],
            "solution": "$$T = 2\\pi \\sqrt{\\frac{0.4}{40}} = 2\\pi \\times 0.1 \\approx 0.6283 \\approx 0.628\\,\\text{s}$$\\nĐáp số: 0.628 s"
        },
        {
            "id": "ex_9_2",
            "type": "easy",
            "q": "Con lắc lò xo ở câu trên dao động với biên độ $A = 5\\,\\text{cm} = 0.05\\,\\text{m}$. Hãy tính cơ năng toàn phần của con lắc theo đơn vị Jun (J).",
            "unit": "J",
            "ans": 0.05,
            "tol": 0.005,
            "hints": ["$E = \\frac{1}{2}k A^2$."],
            "solution": "$$E = \\frac{1}{2} \\times 40 \\times (0.05)^2 = 20 \\times 0.0025 = 0.05\\,\\text{J}$$\\nĐáp số: 0.05 J"
        },
        {
            "id": "ex_9_3",
            "type": "easy",
            "q": "Tính tốc độ cực đại $v_{\\max}$ của vật nặng trong con lắc ở câu 2 khi nó đi qua vị trí cân bằng (m/s).",
            "unit": "m/s",
            "ans": 0.5,
            "tol": 0.02,
            "hints": ["$v_{\\max} = A \\omega_0$ với $\\omega_0 = 10\\,\\text{rad/s}$."],
            "solution": "$$v_{\\max} = 0.05 \\times 10 = 0.5\\,\\text{m/s}$$\\nĐáp số: 0.5 m/s"
        },
        {
            "id": "ex_9_4",
            "type": "easy",
            "q": "Một con lắc đơn có chiều dài dây treo $\\ell = 0.98\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính chu kỳ dao động nhỏ của con lắc theo giây.",
            "unit": "s",
            "ans": 1.99,
            "tol": 0.02,
            "hints": ["$T = 2\\pi \\sqrt{\\ell/g}$."],
            "solution": "$$T = 2\\pi \\sqrt{\\frac{0.98}{9.8}} = 2\\pi \\sqrt{0.1} \\approx 1.9869 \\approx 1.99\\,\\text{s}$$\\nĐáp số: 1.99 s"
        },
        {
            "id": "ex_9_5",
            "type": "mid",
            "q": "Con lắc dao động với tần số góc $\\omega = 10\\,\\text{rad/s}$ và biên độ $A = 5\\,\\text{cm} = 0.05\\,\\text{m}$. Tại li độ $x = 3\\,\\text{cm} = 0.03\\,\\text{m}$, vận tốc của vật có độ lớn bằng bao nhiêu m/s?",
            "unit": "m/s",
            "ans": 0.4,
            "tol": 0.02,
            "hints": ["$v = \\omega \\sqrt{A^2 - x^2}$."],
            "solution": "$$v = 10 \\times \\sqrt{0.05^2 - 0.03^2} = 10 \\times 0.04 = 0.4\\,\\text{m/s}$$\\nĐáp số: 0.4 m/s"
        },
        {
            "id": "ex_9_6",
            "type": "mid",
            "q": "Tổng hợp hai dao động điều hòa cùng phương cùng tần số: $x_1 = 3\\cos(10t)\\,\\text{cm}$ và $x_2 = 4\\cos(10t + \\pi/2)\\,\\text{cm}$. Biên độ của dao động tổng hợp bằng bao nhiêu cm?",
            "unit": "cm",
            "ans": 5.0,
            "tol": 0.05,
            "hints": ["Hai dao động vuông pha (độ lệch pha $\\pi/2$), $A = \\sqrt{A_1^2 + A_2^2}$."],
            "solution": "$$A = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5.0\\,\\text{cm}$$\\nĐáp số: 5.0 cm"
        },
        {
            "id": "ex_9_7",
            "type": "mid",
            "q": "Hai âm thoa phát ra hai sóng âm có tần số lần lượt là $f_1 = 440\\,\\text{Hz}$ và $f_2 = 444\\,\\text{Hz}$. Số phách nghe được trong 1 giây (tần số phách) bằng bao nhiêu Hz?",
            "unit": "Hz",
            "ans": 4.0,
            "tol": 0.05,
            "hints": ["$f_{ph} = |f_1 - f_2|$."],
            "solution": "$$f_{ph} = |444 - 440| = 4.0\\,\\text{Hz}$$\\nĐáp số: 4.0 Hz"
        },
        {
            "id": "ex_9_8",
            "type": "mid",
            "q": "Một thanh đồng chất mảnh dài $\\ell = 1.0\\,\\text{m}$ dao động quanh trục nằm ngang qua một đầu ($I = \\frac{1}{3}m\\ell^2, d = \\ell/2$). Lấy $g = 9.8\\,\\text{m/s}^2$. Tính chu kỳ dao động nhỏ của con lắc vật lý này theo giây.",
            "unit": "s",
            "ans": 1.64,
            "tol": 0.02,
            "hints": ["$T = 2\\pi \\sqrt{\\frac{2\\ell}{3g}}$."],
            "solution": "$$T = 2\\pi \\sqrt{\\frac{2 \\times 1.0}{3 \\times 9.8}} = 2\\pi \\sqrt{\\frac{2}{29.4}} \\approx 1.639 \\approx 1.64\\,\\text{s}$$\\nĐáp số: 1.64 s"
        },
        {
            "id": "ex_9_9",
            "type": "hard",
            "q": "Một hệ dao động có tần số góc riêng $\\omega_0 = 100\\,\\text{rad/s}$ và hệ số tắt dần $\\gamma = 0.5\\,\\text{s}^{-1}$. Hãy tính hệ số phẩm chất $Q$ của hệ dao động này.",
            "unit": "",
            "ans": 100.0,
            "tol": 0.5,
            "hints": ["$Q = \\frac{\\omega_0}{2\\gamma}$."],
            "solution": "$$Q = \\frac{100}{2 \\times 0.5} = \\frac{100}{1.0} = 100.0$$\\nĐáp số: 100.0"
        },
        {
            "id": "ex_9_10",
            "type": "hard",
            "q": "Một hệ dao động có $m = 0.5\\,\\text{kg}$, độ cứng $k = 50\\,\\text{N/m}$ ($\omega_0 = 10\\,\\text{rad/s}$), hệ số cản nhớt $b = 0.4\\,\\text{kg/s}$. Khi chịu ngoại lực điều hòa có biên độ $F_0 = 2.0\\,\\text{N}$, biên độ dao động tại cộng hưởng $A_{\\max} \\approx \\frac{F_0}{b\\omega_0}$ bằng bao nhiêu mét?",
            "unit": "m",
            "ans": 0.5,
            "tol": 0.02,
            "hints": ["$A_{\\max} = \\frac{F_0}{b \\omega_0} = \\frac{2.0}{0.4 \\times 10}$."],
            "solution": "$$A_{\\max} = \\frac{2.0}{0.4 \\times 10} = \\frac{2.0}{4.0} = 0.5\\,\\text{m}$$\\nĐáp số: 0.5 m"
        }
    ]
}

CH10 = {
    "id": 10,
    "num": 10,
    "part": "Phần II — Dao động và Sóng cơ",
    "title": "Sóng cơ",
    "tag": "Giao thoa, Sóng dừng & Doppler",
    "status": "ready",
    "summary": "Phương trình sóng cơ 1 chiều, tốc độ truyền sóng trong các môi trường, năng lượng sóng và mức cường độ âm (dB), giao thoa sóng, sóng dừng, hiệu ứng Doppler và nguyên lý Huygens.",
    "nature": {
        "why": "Sóng là cơ chế lan truyền dao động và vận chuyển năng lượng qua không gian mà không có sự vận chuyển của vật chất.",
        "meaning": "Mỗi phần tử môi trường chỉ dao động tại chỗ quanh vị trí cân bằng. Sóng truyền pha dao động trễ dần theo khoảng cách. Sóng dừng là hiện tượng giao thoa của hai sóng cùng biên độ ngược chiều, tạo nên các nút cố định (năng lượng bị giam hãm tại chỗ). Hiệu ứng Doppler phản ánh sự thay đổi tần số biểu kiến do chuyển động tương đối giữa nguồn phát và người quan sát.",
        "conditions": "Môi trường truyền sóng phải có tính đàn hồi và liên tục (chất rắn, lỏng, khí). Sóng cơ không truyền được trong chân không.",
        "limits": "Khi biên độ sóng quá lớn, môi trường mất tính đàn hồi tuyến tính và phương trình sóng trở thành phi tuyến, sinh ra sóng xung kích (shockwave)."
    },
    "formulas": [
        {
            "name": "Phương trình Sóng Điều hòa và Phương trình Vi phân Sóng",
            "latex": "u(x, t) = A\\cos(\\omega t - kx + \\varphi_0); \\quad k = \\frac{2\\pi}{\\lambda}; \\quad v = \\frac{\\omega}{k} = \\lambda f; \\quad \\frac{\\partial^2 u}{\\partial t^2} = v^2 \\frac{\\partial^2 u}{\\partial x^2}",
            "meaning": "Độ lệch pha giữa hai điểm cách nhau $\\Delta x$ trên phương truyền sóng là $\\Delta\\Phi = k\\Delta x = \\frac{2\\pi \\Delta x}{\\lambda}$.",
            "proof": [
                {"step": "u(x, t) = u\\left(0, t - \\frac{x}{v}\\right)", "reason": "Dao động tại x trễ hơn tại gốc một khoảng thời gian truyền sóng Δt = x/v"},
                {"step": "u(x, t) = A\\cos\\left[\\omega\\left(t - \\frac{x}{v}\\right) + \\varphi_0\\right] = A\\cos(\\omega t - kx + \\varphi_0)", "reason": "Thay biểu thức pha với số sóng k = ω/v = 2π/λ"},
                {"step": "\\frac{\\partial^2 u}{\\partial t^2} = -\\omega^2 u, \\quad \\frac{\\partial^2 u}{\\partial x^2} = -k^2 u", "reason": "Lấy đạo hàm riêng cấp 2 theo thời gian t và tọa độ x"},
                {"step": "\\frac{\\partial^2 u}{\\partial t^2} = \\frac{\\omega^2}{k^2}\\frac{\\partial^2 u}{\\partial x^2} = v^2 \\frac{\\partial^2 u}{\\partial x^2}", "reason": "Đồng nhất hệ thức vận tốc pha v = ω/k"}
            ]
        },
        {
            "name": "Cường độ Âm, Mức Cường độ Âm và Sóng dừng",
            "latex": "I = \\frac{1}{2}\\rho v \\omega^2 A^2; \\quad L = 10\\lg\\left(\\frac{I}{I_0}\\right)\\,(\\text{dB}); \\quad L_{dây} = n\\frac{\\lambda}{2} \\implies f_n = n\\frac{v}{2L}",
            "meaning": "Mức cường độ âm dùng thang đo logarit (tăng 10 dB tương ứng cường độ tăng gấp 10 lần). Sóng dừng trên dây hai đầu cố định chỉ tồn tại các họa âm nguyên lần âm cơ bản.",
            "proof": [
                {"step": "u = A\\cos(\\omega t - kx) + A\\cos(\\omega t + kx)", "reason": "Tổng hợp sóng tới và sóng phản xạ cùng biên độ truyền ngược chiều"},
                {"step": "u = 2A\\cos(kx)\\cos(\\omega t)", "reason": "Áp dụng công thức cộng lượng giác: cos a + cos b = 2 cos((a-b)/2) cos((a+b)/2)"},
                {"step": "|2A\\cos(kx)| = 0 \\implies kx = \\left(n + \\frac{1}{2}\\right)\\pi \\implies x_{nút} = \\left(n + \\frac{1}{2}\\right)\\frac{\\lambda}{2}", "reason": "Vị trí các điểm nút dao động triệt tiêu"}
            ]
        },
        {
            "name": "Hiệu ứng Doppler cho Sóng Âm",
            "latex": "f' = f \\frac{v + v_o}{v - v_s}; \\quad \\sin\\alpha = \\frac{v}{v_s} \\; (\\text{Góc nón Mach})",
            "meaning": "Quy ước dấu: $v_o > 0$ khi người quan sát tiến lại gần nguồn; $v_s > 0$ khi nguồn tiến lại gần người quan sát. Khi $v_s > v$, hình thành sóng xung kích hình nón Mach.",
            "proof": [
                {"step": "\\lambda' = \\frac{v - v_s}{f}", "reason": "Nguồn tiến lại làm bước sóng phía trước bị nén lại"},
                {"step": "f' = \\frac{v_{tương\\,đối}}{\\lambda'} = \\frac{v + v_o}{\\lambda'} = f \\frac{v + v_o}{v - v_s}", "reason": "Người quan sát chuyển động đón đầu các mặt sóng"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Viết phương trình sóng, độ lệch pha và mức cường độ âm",
            "algorithm": [
                "Bước 1: Tính bước sóng $\\lambda = v/f = v T$.",
                "Bước 2: Viết phương trình sóng tại điểm cách nguồn $x$: $u_M = A\\cos(\\omega t - \\frac{2\\pi x}{\\lambda} + \\varphi_0)$.",
                "Bước 3: Độ lệch pha: $\\Delta\\varphi = \\frac{2\\pi \\Delta x}{\\lambda}$. Hai điểm cùng pha khi $\\Delta x = k\\lambda$, ngược pha khi $\\Delta x = (k + 0.5)\\lambda$.",
                "Bước 4: Mức cường độ âm: $L_1 - L_2 = 20\\lg(r_2 / r_1)$ đối với nguồn âm điểm trong không gian."
            ]
        },
        {
            "name": "Dạng 2: Sóng dừng và Hiệu ứng Doppler",
            "algorithm": [
                "Bước 1: Sóng dừng: Hai đầu cố định $\\implies L = n\\frac{\\lambda}{2}$; Một đầu cố định một đầu hở $\\implies L = (2n - 1)\\frac{\\lambda}{4}$.",
                "Bước 2: Khoảng cách giữa 2 nút hoặc 2 bụng liên tiếp là $\\lambda/2$; giữa nút và bụng kề nhau là $\\lambda/4$.",
                "Bước 3: Hiệu ứng Doppler: Xác định chiều chuyển động của nguồn và người để gán đúng dấu trong công thức $f' = f\\frac{v \\pm v_o}{v \\mp v_s}$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Giao thoa sóng trên mặt nước",
            "problem": "Hai nguồn sóng kết hợp $S_1, S_2$ cách nhau $12\\,\\text{cm}$ dao động cùng pha với tần số $f = 20\\,\\text{Hz}$. Tốc độ truyền sóng trên mặt nước là $v = 40\\,\\text{cm/s}$. Hỏi trên đoạn nối hai nguồn $S_1 S_2$ có bao nhiêu điểm dao động với biên độ cực đại?",
            "analysis": "Bước sóng $\\lambda = v/f = 2\\,\\text{cm}$. Điều kiện cực đại giao thoa cùng pha: $d_2 - d_1 = k\\lambda$.",
            "solution": "1. Tính bước sóng:\\n$$\\lambda = \\frac{v}{f} = \\frac{40}{20} = 2.0\\,\\text{cm}$$\\n2. Vị trí cực đại trên đoạn thẳng nối hai nguồn:\\n$$-S_1 S_2 < k\\lambda < S_1 S_2 \\implies -12 < 2k < 12 \\implies -6 < k < 6$$\\nVì $k$ nguyên: $k \\in \\{-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5\\}$.\\nTổng số cực đại là $5 - (-5) + 1 = 11$ điểm.\\nĐáp số: Có 11 điểm dao động cực đại."
        }
    ],
    "pitfalls": [
        {
            "error": "Nhầm lẫn giữa tốc độ truyền sóng v và tốc độ dao động của phần tử môi trường u'(t)",
            "fix": "Tốc độ truyền sóng $v = \\lambda f$ là tốc độ lan truyền pha dao động trong môi trường (hằng số). Tốc độ dao động của phần tử $v_{pt} = -A\\omega\\sin(\\dots)$ biến thiên điều hòa theo thời gian với cực đại là $A\\omega$.",
            "tip": "Sóng cơ truyền đi nhưng phần tử môi trường chỉ dao động tại chỗ quanh vị trí cân bằng."
        }
    ],
    "exercises": [
        {
            "id": "ex_10_1",
            "type": "easy",
            "q": "Một sóng cơ có tần số $f = 250\\,\\text{Hz}$ và bước sóng $\\lambda = 1.36\\,\\text{m}$. Hãy tính tốc độ truyền sóng trong môi trường theo m/s.",
            "unit": "m/s",
            "ans": 340.0,
            "tol": 1.0,
            "hints": ["$v = \\lambda f$."],
            "solution": "$$v = 1.36 \\times 250 = 340.0\\,\\text{m/s}$$\\nĐáp số: 340.0 m/s"
        },
        {
            "id": "ex_10_2",
            "type": "easy",
            "q": "Một sợi dây đàn hồi có mật độ khối lượng dài $\\mu = 0.01\\,\\text{kg/m}$ được kéo căng với lực căng $T = 100\\,\\text{N}$. Tính tốc độ truyền sóng ngang trên sợi dây.",
            "unit": "m/s",
            "ans": 100.0,
            "tol": 1.0,
            "hints": ["$v = \\sqrt{T/\\mu}$."],
            "solution": "$$v = \\sqrt{\\frac{100}{0.01}} = \\sqrt{10000} = 100.0\\,\\text{m/s}$$\\nĐáp số: 100.0 m/s"
        },
        {
            "id": "ex_10_3",
            "type": "easy",
            "q": "Cường độ âm tại một điểm đo được là $I = 10^{-6}\\,\\text{W/m}^2$. Cho cường độ âm chuẩn $I_0 = 10^{-12}\\,\\text{W/m}^2$. Tính mức cường độ âm $L$ theo đơn vị Decibel (dB).",
            "unit": "dB",
            "ans": 60.0,
            "tol": 0.5,
            "hints": ["$L = 10 \\lg(I/I_0)$."],
            "solution": "$$L = 10 \\lg\\left(\\frac{10^{-6}}{10^{-12}}\\right) = 10 \\lg(10^6) = 10 \\times 6 = 60.0\\,\\text{dB}$$\\nĐáp số: 60.0 dB"
        },
        {
            "id": "ex_10_4",
            "type": "easy",
            "q": "Một sợi dây đàn dài $L = 1.0\\,\\text{m}$ có hai đầu cố định, vận tốc truyền sóng trên dây là $v = 100\\,\\text{m/s}$. Tần số âm cơ bản (họa âm bậc 1) phát ra bằng bao nhiêu Hz?",
            "unit": "Hz",
            "ans": 50.0,
            "tol": 0.5,
            "hints": ["$f_1 = \\frac{v}{2L}$."],
            "solution": "$$f_1 = \\frac{100}{2 \\times 1.0} = 50.0\\,\\text{Hz}$$\\nĐáp số: 50.0 Hz"
        },
        {
            "id": "ex_10_5",
            "type": "mid",
            "q": "Một sóng cơ có bước sóng $\\lambda = 0.8\\,\\text{m}$. Hai điểm nằm trên cùng một phương truyền sóng cách nhau $\\Delta x = 0.2\\,\\text{m}$. Độ lệch pha giữa dao động của hai điểm này bằng bao nhiêu độ?",
            "unit": "độ",
            "ans": 90.0,
            "tol": 0.5,
            "hints": ["$\\Delta\\varphi = \\frac{2\\pi \\Delta x}{\\lambda}$ rad. Đổi sang độ: $\\Delta\\varphi^\\circ = \\frac{360^\\circ \\Delta x}{\\lambda}$."],
            "solution": "$$\\Delta\\varphi = \\frac{360^\\circ \\times 0.2}{0.8} = \\frac{360^\\circ}{4} = 90.0^\\circ$$\\nĐáp số: 90.0 độ"
        },
        {
            "id": "ex_10_6",
            "type": "mid",
            "q": "Tại điểm cách một nguồn âm điểm khoảng cách $r_1 = 2.0\\,\\text{m}$, mức cường độ âm là $L_1 = 70\\,\\text{dB}$. Khi ra xa nguồn đến khoảng cách $r_2 = 20.0\\,\\text{m}$, mức cường độ âm $L_2$ bằng bao nhiêu dB?",
            "unit": "dB",
            "ans": 50.0,
            "tol": 0.5,
            "hints": ["$L_2 = L_1 - 20\\lg(r_2 / r_1)$."],
            "solution": "$$L_2 = 70 - 20\\lg\\left(\\frac{20}{2}\\right) = 70 - 20\\lg(10) = 70 - 20 = 50.0\\,\\text{dB}$$\\nĐáp số: 50.0 dB"
        },
        {
            "id": "ex_10_7",
            "type": "mid",
            "q": "Hai nguồn sóng kết hợp cùng pha có bước sóng $\\lambda = 4.0\\,\\text{cm}$. Một điểm M trong vùng giao thoa cách hai nguồn các khoảng $d_1 = 22.0\\,\\text{cm}$ và $d_2 = 30.0\\,\\text{cm}$. Điểm M là cực đại giao thoa bậc mấy?",
            "unit": "bậc",
            "ans": 2.0,
            "tol": 0.05,
            "hints": ["Hiệu đường đi: $\\Delta d = d_2 - d_1 = 8.0\\,\\text{cm}$.", "Bậc cực đại: $k = \\Delta d / \\lambda$."],
            "solution": "$$k = \\frac{d_2 - d_1}{\\lambda} = \\frac{30.0 - 22.0}{4.0} = \\frac{8.0}{4.0} = 2.0$$\\nĐáp số: 2.0"
        },
        {
            "id": "ex_10_8",
            "type": "mid",
            "q": "Một ống sáo một đầu kín, một đầu hở có chiều dài $L = 0.85\\,\\text{m}$. Tốc độ truyền âm trong không khí là $v = 340\\,\\text{m/s}$. Tần số âm cơ bản phát ra từ ống sáo là bao nhiêu Hz?",
            "unit": "Hz",
            "ans": 100.0,
            "tol": 1.0,
            "hints": ["Ống sáo 1 đầu kín: $f_1 = \\frac{v}{4L}$."],
            "solution": "$$f_1 = \\frac{340}{4 \\times 0.85} = \\frac{340}{3.4} = 100.0\\,\\text{Hz}$$\\nĐáp số: 100.0 Hz"
        },
        {
            "id": "ex_10_9",
            "type": "hard",
            "q": "Xe cứu thương phát còi tần số $f = 600\\,\\text{Hz}$ chạy với tốc độ $v_s = 20\\,\\text{m/s}$ tiến lại gần một ô tô đang chạy ngược chiều với tốc độ $v_o = 15\\,\\text{m/s}$. Vận tốc âm trong không khí là $v = 340\\,\\text{m/s}$. Tần số âm mà người trong ô tô nghe được là bao nhiêu Hz? (Làm tròn 1 chữ số thập phân).",
            "unit": "Hz",
            "ans": 665.6,
            "tol": 1.0,
            "hints": ["Công thức Doppler khi hai xe cùng lại gần nhau: $f' = f \\frac{v + v_o}{v - v_s}$."],
            "solution": "$$f' = 600 \\times \\frac{340 + 15}{340 - 20} = 600 \\times \\frac{355}{320} \\approx 665.625 \\approx 665.6\\,\\text{Hz}$$\\nĐáp số: 665.6 Hz"
        },
        {
            "id": "ex_10_10",
            "type": "hard",
            "q": "Một máy bay bay siêu thanh với vận tốc $v_s = 680\\,\\text{m/s}$ trong không khí có tốc độ âm $v = 340\\,\\text{m/s}$. Tính góc nửa mở $\\alpha$ của mặt nón sóng Mach (độ).",
            "unit": "độ",
            "ans": 30.0,
            "tol": 0.5,
            "hints": ["$\\sin\\alpha = \\frac{v}{v_s} = \\frac{340}{680} = 0.5$."],
            "solution": "$$\\sin\\alpha = \\frac{340}{680} = 0.5 \\implies \\alpha = 30.0^\\circ$$\\nĐáp số: 30.0 độ"
        }
    ]
}

print("Chapters 9, 10 data module ready.")
