# -*- coding: utf-8 -*-
"""
Module defining data for Chapter 11, 12, 13, 14 (Nhiệt học)
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

CH11 = {
    "id": 11,
    "num": 11,
    "part": "Phần III — Nhiệt học",
    "title": "Khí lý tưởng và Thuyết động học phân tử",
    "tag": "Phân bố Maxwell - Boltzmann",
    "status": "ready",
    "summary": "Phương trình trạng thái Clapeyron-Mendeleev, áp suất và nhiệt độ theo thuyết động học, định lý phân bố đều năng lượng theo bậc tự do, phân bố Maxwell về vận tốc, phân bố độ cao Boltzmann, quãng đường tự do trung bình và các hiện tượng vận chuyển.",
    "nature": {
        "why": "Để giải thích các thông số trạng thái vĩ mô (áp suất, thể tích, nhiệt độ) từ chuyển động hỗn loạn nhiệt vi mô của hàng tỷ phân tử.",
        "meaning": "Áp suất là kết quả của vô số va chạm đàn hồi của phân tử lên thành bình ($p = \\frac{2}{3}n_0\\bar{\\varepsilon}_d$). Nhiệt độ tuyệt đối $T$ là thước đo trực tiếp động năng tịnh tiến trung bình ($\\bar{\\varepsilon}_d = \\frac{3}{2}kT$). Nội năng chỉ phụ thuộc nhiệt độ.",
        "conditions": "Khí lý tưởng: Thể tích riêng phân tử coi như bằng 0, không có lực tương tác từ xa trừ lúc va chạm.",
        "limits": "Khi nhiệt độ rất thấp hoặc áp suất rất cao, mật độ phân tử dày đặc, thể tích riêng và lực hút phân tử không thể bỏ qua, phải dùng mô hình Khí thực Van der Waals."
    },
    "formulas": [
        {
            "name": "Phương trình Clapeyron - Mendeleev và Áp suất Động học",
            "latex": "pV = nRT = NkT; \\quad p = \\frac{1}{3}n_0 m_0 \\overline{v^2} = \\frac{2}{3}n_0 \\langle\\varepsilon_d\\rangle; \\quad \\langle\\varepsilon_d\\rangle = \\frac{3}{2}kT",
            "meaning": "Mối liên hệ giữa áp suất $p$ và động năng tịnh tiến trung bình. $k = R/N_A = 1.38 \\times 10^{-23}\\,\\text{J/K}$.",
            "proof": [
                {"step": "\\Delta p_x = 2 m_0 v_x", "reason": "Xung lượng truyền cho thành bình khi một phân tử va chạm đàn hồi vuông góc"},
                {"step": "p = \\frac{1}{A dt}\\sum 2 m_0 v_x \\cdot \\frac{1}{2}n_0 A v_x dt = n_0 m_0 \\overline{v_x^2}", "reason": "Cộng dồn tất cả các phân tử bay về phía thành bình trong thời gian dt"},
                {"step": "\\overline{v_x^2} = \\overline{v_y^2} = \\overline{v_z^2} = \\frac{1}{3}\\overline{v^2}", "reason": "Tính chất đẳng hướng của chuyển động nhiệt trong không gian 3 chiều"},
                {"step": "p = \\frac{1}{3}n_0 m_0 \\overline{v^2} = \\frac{2}{3}n_0 \\left(\\frac{1}{2}m_0 \\overline{v^2}\\right) = \\frac{2}{3}n_0 \\langle\\varepsilon_d\\rangle", "reason": "Đưa về dạng biểu thức động năng tịnh tiến trung bình"}
            ]
        },
        {
            "name": "Ba Vận tốc đặc trưng Maxwell và Phân bố Vận tốc",
            "latex": "v_p = \\sqrt{\\frac{2RT}{M}}; \\quad \\bar{v} = \\sqrt{\\frac{8RT}{\\pi M}}; \\quad v_{rms} = \\sqrt{\\frac{3RT}{M}}; \\quad v_p < \\bar{v} < v_{rms}",
            "meaning": "$v_p$ là vận tốc xác suất lớn nhất (đỉnh của hàm phân bố Maxwell). $v_{rms}$ là vận tốc căn quân phương.",
            "proof": [
                {"step": "F(v) = 4\\pi\\left(\\frac{m_0}{2\\pi kT}\\right)^{3/2} v^2 \\exp\\left(-\\frac{m_0 v^2}{2kT}\\right)", "reason": "Hàm mật độ phân bố vận tốc Maxwell"},
                {"step": "\\frac{dF}{dv} = 0 \\implies \\frac{d}{dv}[v^2 e^{-a v^2}] = 0 \\implies 2v - 2a v^3 = 0 \\implies v_p = \\sqrt{\\frac{1}{a}} = \\sqrt{\\frac{2kT}{m_0}}", "reason": "Tìm điểm cực đại của hàm phân bố"},
                {"step": "\\bar{v} = \\int_0^\\infty v F(v)dv = \\sqrt{\\frac{8RT}{\\pi M}}, \\quad v_{rms} = \\sqrt{\\int_0^\\infty v^2 F(v)dv} = \\sqrt{\\frac{3RT}{M}}", "reason": "Tính các mômen thống kê trung bình"}
            ]
        },
        {
            "name": "Phân bố Boltzmann và Quãng đường tự do trung bình",
            "latex": "p(h) = p_0 e^{-\\frac{Mgh}{RT}}; \\quad \\bar{\\lambda} = \\frac{1}{\\sqrt{2}\\pi d^2 n_0} = \\frac{kT}{\\sqrt{2}\\pi d^2 p}",
            "meaning": "Áp suất khí quyển giảm theo hàm mũ theo độ cao. $\\bar{\\lambda}$ là quãng đường trung bình phân tử đi được giữa hai va chạm liên tiếp.",
            "proof": [
                {"step": "dp = -\\rho g dh = -\\frac{p M}{RT}g dh \\implies \\frac{dp}{p} = -\\frac{Mg}{RT}dh", "reason": "Cân bằng thủy tĩnh trong khí quyển đẳng nhiệt"},
                {"step": "\\int_{p_0}^p \\frac{dp'}{p'} = -\\frac{Mg}{RT}\\int_0^h dh' \\implies p(h) = p_0 e^{-\\frac{Mgh}{RT}}", "reason": "Tích phân hai vế thu được công thức khí áp Boltzmann"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Phương trình trạng thái, nội năng và bậc tự do",
            "algorithm": [
                "Bước 1: Xác định số bậc tự do: Đơn nguyên tử $i = 3$; Lưỡng nguyên tử $i = 5$; Đa nguyên tử $i = 6$.",
                "Bước 2: Nội năng $U = \\frac{i}{2}nRT = \\frac{i}{2}pV$.",
                "Bước 3: Nhiệt dung mol: $C_v = \\frac{i}{2}R$, $C_p = \\frac{i+2}{2}R$, $\\gamma = \\frac{i+2}{i}$.",
                "Bước 4: Kiểm tra thứ nguyên Jun [J]."
            ]
        },
        {
            "name": "Dạng 2: Tính các vận tốc phân tử Maxwell và quãng đường tự do",
            "algorithm": [
                "Bước 1: Đổi khối lượng mol sang kg/mol (ví dụ $O_2: 32 \\times 10^{-3}\\,\\text{kg/mol}$).",
                "Bước 2: Áp dụng $v_p = \\sqrt{2RT/M}$, $\\bar{v} = \\sqrt{8RT/(\\pi M)}$, $v_{rms} = \\sqrt{3RT/M}$.",
                "Bước 3: Tính mật độ phân tử $n_0 = p / (kT)$, sau đó tính $\\bar{\\lambda} = \\frac{1}{\\sqrt{2}\\pi d^2 n_0}$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Tính vận tốc căn quân phương của phân tử khí Oxy",
            "problem": "Tính vận tốc căn quân phương $v_{rms}$ của phân tử khí Oxy ($O_2$, khối lượng mol $M = 32\\,\\text{g/mol} = 0.032\\,\\text{kg/mol}$) ở nhiệt độ $T = 300\\,\\text{K}$.",
            "analysis": "Áp dụng trực tiếp công thức $v_{rms} = \\sqrt{3RT/M}$.",
            "solution": "$$v_{rms} = \\sqrt{\\frac{3 \\times 8.314 \\times 300}{0.032}} = \\sqrt{\\frac{7482.6}{0.032}} = \\sqrt{233831.25} \\approx 483.56\\,\\text{m/s} \\approx 483.6\\,\\text{m/s}$$\\nĐáp số: 483.6 m/s."
        }
    ],
    "pitfalls": [
        {
            "error": "Quên đổi nhiệt độ từ °C sang Kelvin: dùng t thay vì T = t + 273.15",
            "fix": "Trong mọi công thức nhiệt động lực học và thuyết động học phân tử, nhiệt độ $T$ bắt buộc phải tính bằng độ tuyệt đối Kelvin.",
            "tip": "$0^\\circ\\text{C} = 273.15\\,\\text{K}$, $27^\\circ\\text{C} = 300.15\\,\\text{K}$."
        }
    ],
    "exercises": [
        {
            "id": "ex_11_1",
            "type": "easy",
            "q": "Một bình thể tích $V = 10\\,\\text{lít} = 0.01\\,\\text{m}^3$ chứa $n = 2\\,\\text{mol}$ khí lý tưởng ở nhiệt độ $T = 300\\,\\text{K}$. Cho $R = 8.314\\,\\text{J/(mol}\\cdot\\text{K)}$. Tính áp suất khí theo kPa.",
            "unit": "kPa",
            "ans": 498.8,
            "tol": 1.0,
            "hints": ["$p = \\frac{nRT}{V}$, đổi Pa sang kPa."],
            "solution": "$$p = \\frac{2 \\times 8.314 \\times 300}{0.01} = 498840\\,\\text{Pa} = 498.8\\,\\text{kPa}$$\\nĐáp số: 498.8 kPa"
        },
        {
            "id": "ex_11_2",
            "type": "easy",
            "q": "Ở nhiệt độ $T = 300\\,\\text{K}$, hằng số Boltzmann $k = 1.38 \\times 10^{-23}\\,\\text{J/K}$. Tính động năng tịnh tiến trung bình của một phân tử khí theo đơn vị $10^{-21}\\,\\text{J}$.",
            "unit": "×10⁻²¹ J",
            "ans": 6.21,
            "tol": 0.05,
            "hints": ["$\\langle\\varepsilon_d\\rangle = \\frac{3}{2}kT$."],
            "solution": "$$\\langle\\varepsilon_d\\rangle = 1.5 \\times 1.38 \\times 10^{-23} \\times 300 = 6.21 \\times 10^{-21}\\,\\text{J}$$\\nĐáp số: 6.21"
        },
        {
            "id": "ex_11_3",
            "type": "easy",
            "q": "Khí Oxy ($M = 0.032\\,\\text{kg/mol}$) ở nhiệt độ $T = 300\\,\\text{K}$. Vận tốc căn quân phương $v_{rms}$ của phân tử Oxy là bao nhiêu m/s?",
            "unit": "m/s",
            "ans": 483.6,
            "tol": 1.0,
            "hints": ["$v_{rms} = \\sqrt{3RT/M}$."],
            "solution": "$$v_{rms} = \\sqrt{\\frac{3 \\times 8.314 \\times 300}{0.032}} \\approx 483.6\\,\\text{m/s}$$\\nĐáp số: 483.6 m/s"
        },
        {
            "id": "ex_11_4",
            "type": "easy",
            "q": "Cho $n = 3\\,\\text{mol}$ khí Heli (đơn nguyên tử, $i = 3$) ở nhiệt độ $T = 400\\,\\text{K}$. Tính nội năng $U$ của khối khí theo đơn vị Jun (J).",
            "unit": "J",
            "ans": 14965.2,
            "tol": 10.0,
            "hints": ["$U = \\frac{3}{2}nRT$."],
            "solution": "$$U = \\frac{3}{2} \\times 3 \\times 8.314 \\times 400 = 14965.2\\,\\text{J}$$\\nĐáp số: 14965.2 J"
        },
        {
            "id": "ex_11_5",
            "type": "mid",
            "q": "Khí Hydro ($M = 0.002\\,\\text{kg/mol}$) ở nhiệt độ $T = 300\\,\\text{K}$. Vận tốc xác suất lớn nhất $v_p$ của phân tử Hydro bằng bao nhiêu m/s?",
            "unit": "m/s",
            "ans": 1579.3,
            "tol": 2.0,
            "hints": ["$v_p = \\sqrt{2RT/M}$."],
            "solution": "$$v_p = \\sqrt{\\frac{2 \\times 8.314 \\times 300}{0.002}} = \\sqrt{2494200} \\approx 1579.3\\,\\text{m/s}$$\\nĐáp số: 1579.3 m/s"
        },
        {
            "id": "ex_11_6",
            "type": "mid",
            "q": "Đường kính hiệu dụng phân tử khí $d = 3.0 \\times 10^{-10}\\,\\text{m}$, mật độ phân tử $n_0 = 2.5 \\times 10^{25}\\,\\text{m}^{-3}$. Tính quãng đường tự do trung bình $\\bar{\\lambda}$ theo đơn vị nanomet (nm).",
            "unit": "nm",
            "ans": 100.0,
            "tol": 1.0,
            "hints": ["$\\bar{\\lambda} = \\frac{1}{\\sqrt{2}\\pi d^2 n_0}$."],
            "solution": "$$\\bar{\\lambda} = \\frac{1}{\\sqrt{2}\\pi \\times (3 \\times 10^{-10})^2 \\times 2.5 \\times 10^{25}} \\approx 1.0 \\times 10^{-7}\\,\\text{m} = 100.0\\,\\text{nm}$$\\nĐáp số: 100.0 nm"
        },
        {
            "id": "ex_11_7",
            "type": "mid",
            "q": "Không khí có khối lượng mol $M = 0.029\\,\\text{kg/mol}$, nhiệt độ $T = 273\\,\\text{K}, g = 9.8\\,\\text{m/s}^2$. Áp suất mặt biển $p_0 = 101.3\\,\\text{kPa}$. Ở độ cao $h = 3000\\,\\text{m}$, áp suất khí quyển $p$ bằng bao nhiêu kPa?",
            "unit": "kPa",
            "ans": 69.6,
            "tol": 0.5,
            "hints": ["$p = p_0 e^{-\\frac{Mgh}{RT}}$."],
            "solution": "$$p = 101.3 \\times e^{-\\frac{0.029 \\times 9.8 \\times 3000}{8.314 \\times 273}} \\approx 101.3 \\times e^{-0.3756} \\approx 69.58 \\approx 69.6\\,\\text{kPa}$$\\nĐáp số: 69.6 kPa"
        },
        {
            "id": "ex_11_8",
            "type": "mid",
            "q": "Khí Nitơ ($N_2$) là chất khí có phân tử lưỡng nguyên tử cứng ($i = 5$). Hãy tính nhiệt dung mol đẳng áp $C_p$ của khí Nitơ theo đơn vị $\\text{J/(mol}\\cdot\\text{K)}$.",
            "unit": "J/(mol·K)",
            "ans": 29.1,
            "tol": 0.1,
            "hints": ["$C_p = \\frac{i+2}{2}R = \\frac{7}{2}R$."],
            "solution": "$$C_p = 3.5 \\times 8.314 = 29.099 \\approx 29.1\\,\\text{J/(mol}\\cdot\\text{K)}$$\\nĐáp số: 29.1"
        },
        {
            "id": "ex_11_9",
            "type": "hard",
            "q": "Tính tỉ số giữa vận tốc căn quân phương $v_{rms}$ và vận tốc xác suất lớn nhất $v_p$ của khí lý tưởng ở cùng một nhiệt độ (làm tròn 3 chữ số thập phân).",
            "unit": "",
            "ans": 1.225,
            "tol": 0.005,
            "hints": ["$\\frac{v_{rms}}{v_p} = \\sqrt{3/2} = \\sqrt{1.5}$."],
            "solution": "$$\\frac{v_{rms}}{v_p} = \\sqrt{\\frac{3}{2}} = \\sqrt{1.5} \\approx 1.2247 \\approx 1.225$$\\nĐáp số: 1.225"
        },
        {
            "id": "ex_11_10",
            "type": "hard",
            "q": "Một phân tử có vận tốc trung bình $\\bar{v} = 450\\,\\text{m/s}$ và quãng đường tự do trung bình $\\bar{\\lambda} = 9.0 \\times 10^{-8}\\,\\text{m}$. Tần số va chạm $z$ của phân tử bằng bao nhiêu nhân $10^9\\,\\text{s}^{-1}$?",
            "unit": "×10⁹ s⁻¹",
            "ans": 5.0,
            "tol": 0.1,
            "hints": ["$z = \\bar{v} / \\bar{\\lambda}$."],
            "solution": "$$z = \\frac{450}{9.0 \\times 10^{-8}} = 5.0 \\times 10^9\\,\\text{s}^{-1}$$\\nĐáp số: 5.0"
        }
    ]
}

CH12 = {
    "id": 12,
    "num": 12,
    "part": "Phần III — Nhiệt học",
    "title": "Nguyên lý thứ nhất của Nhiệt động lực học",
    "tag": "Công, Nhiệt, Nội năng & Đa phương",
    "status": "ready",
    "summary": "Công và nhiệt lượng, nội năng, định luật bảo toàn năng lượng trong nhiệt học, hệ thức Mayer, các quá trình cân bằng (đẳng tích, đẳng áp, đẳng nhiệt, đoạn nhiệt Poisson) và quá trình đa phương tổng quát.",
    "nature": {
        "why": "Mở rộng định luật bảo toàn năng lượng cho các hệ có trao đổi nhiệt năng và sinh công cơ học.",
        "meaning": "Nội năng $U$ là hàm trạng thái (chỉ phụ thuộc trạng thái đầu - cuối). Công $W$ và nhiệt lượng $Q$ là hàm quá trình (phụ thuộc đường đi). Bác bỏ khả năng chế tạo động cơ vĩnh cửu loại 1 (sinh công mà không tiêu tốn năng lượng).",
        "conditions": "Hệ nhiệt động kín thực hiện các quá trình biến đổi chuẩn tĩnh.",
        "limits": "Nguyên lý I chỉ đảm bảo năng lượng bảo toàn nhưng không chỉ ra chiều tự phát của quá trình (cần đến Nguyên lý II)."
    },
    "formulas": [
        {
            "name": "Nguyên lý I Nhiệt động lực học và Công giãn nở",
            "latex": "\\Delta U = Q - W; \\quad dU = \\delta Q - pdV; \\quad W = \\int_{V_1}^{V_2} pdV",
            "meaning": "Độ biến thiên nội năng bằng nhiệt lượng nhận được trừ đi công do chất khí sinh ra ($W > 0$ khi khí dãn nở).",
            "proof": [
                {"step": "\\delta W = F dx = (pA)dx = p (A dx) = p dV", "reason": "Lực áp suất đẩy piston dịch chuyển vi phân dx"},
                {"step": "W = \\int_{V_1}^{V_2} p dV", "reason": "Tích phân công bằng diện tích dưới đường cong trên đồ thị p-V"},
                {"step": "dU = \\delta Q - \\delta W = \\delta Q - p dV", "reason": "Dạng vi phân của nguyên lý I nhiệt động lực học"}
            ]
        },
        {
            "name": "Nhiệt dung mol và Hệ thức Mayer",
            "latex": "C_V = \\frac{i}{2}R; \\quad C_p = C_V + R = \\frac{i+2}{2}R; \\quad \\Delta U = n C_V \\Delta T",
            "meaning": "Đẳng áp cần nhiều nhiệt hơn đẳng tích một lượng đúng bằng $R$ vì phải cấp thêm năng lượng để khí dãn nở sinh công chống ngoại lực.",
            "proof": [
                {"step": "\\delta Q_V = dU = n C_V dT", "reason": "Trong quá trình đẳng tích dV = 0 nên δW = 0"},
                {"step": "\\delta Q_p = dU + p dV = n C_V dT + n R dT = n(C_V + R)dT", "reason": "Trong quá trình đẳng áp pdV = nRdT từ pV = nRT"},
                {"step": "C_p = \\frac{\\delta Q_p}{n dT} = C_V + R", "reason": "Hệ thức Mayer cho khí lý tưởng"}
            ]
        },
        {
            "name": "Phương trình Đoạn nhiệt Poisson và Quá trình Đa phương",
            "latex": "pV^\\gamma = \\text{const}; \\quad T V^{\\gamma - 1} = \\text{const}; \\quad pV^m = \\text{const}; \\quad C_m = C_V - \\frac{R}{m - 1}",
            "meaning": "Trong quá trình đoạn nhiệt ($Q = 0$), công sinh ra hoàn toàn do tiêu hao nội năng làm khí lạnh đi ($W = -\\Delta U$).",
            "proof": [
                {"step": "\\delta Q = 0 \\implies n C_V dT = -p dV = -\\frac{nRT}{V}dV", "reason": "Nguyên lý I trong điều kiện cách nhiệt δQ = 0"},
                {"step": "\\frac{dT}{T} + (\\gamma - 1)\\frac{dV}{V} = 0", "reason": "Sử dụng quan hệ R/C_V = γ - 1"},
                {"step": "\\ln T + (\\gamma - 1)\\ln V = \\text{const} \\implies T V^{\\gamma - 1} = \\text{const}", "reason": "Tích phân hai vế thu được phương trình Poisson"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Tính công, nhiệt và biến thiên nội năng trong 4 quá trình cân bằng",
            "algorithm": [
                "Bước 1: Đẳng tích ($V=\\text{const}$): $W = 0, Q = \\Delta U = n C_V \\Delta T$.",
                "Bước 2: Đẳng áp ($p=\\text{const}$): $W = p\\Delta V = n R \\Delta T, Q = n C_p \\Delta T, \\Delta U = n C_V \\Delta T$.",
                "Bước 3: Đẳng nhiệt ($T=\\text{const}$): $\\Delta U = 0, Q = W = nRT\\ln(V_2/V_1)$.",
                "Bước 4: Đoạn nhiệt ($Q=0$): $Q = 0, W = -\\Delta U = -n C_V \\Delta T = \\frac{p_1 V_1 - p_2 V_2}{\\gamma - 1}$."
            ]
        },
        {
            "name": "Dạng 2: Tính công và hiệu suất của chu trình kín",
            "algorithm": [
                "Bước 1: Vẽ đồ thị chu trình trên hệ tọa độ p-V. Công $W$ bằng diện tích chu trình (dương nếu theo chiều kim đồng hồ).",
                "Bước 2: Tìm các giai đoạn khí nhận nhiệt ($Q > 0$) để tính tổng nhiệt nhận $Q_1 = \\sum Q_{nhan}$.",
                "Bước 3: Hiệu suất chu trình: $\\eta = \\frac{W}{Q_1} = \\frac{Q_1 - |Q_2|}{Q_1}$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Nén đoạn nhiệt không khí",
            "problem": "Nén đoạn nhiệt $1\\,\\text{mol}$ không khí ($\gamma = 1.4$) từ nhiệt độ ban đầu $T_1 = 300\\,\\text{K}$, thể tích giảm còn $1/10$ ($V_1/V_2 = 10$). Tính nhiệt độ cuối $T_2$ và công khí nhận được.",
            "analysis": "Sử dụng $T_2 = T_1(V_1/V_2)^{\gamma - 1}$ và công nhận $|W| = \\Delta U = n C_v(T_2 - T_1)$.",
            "solution": "1. Nhiệt độ cuối sau khi nén:\\n$$T_2 = T_1 \\left(\\frac{V_1}{V_2}\\right)^{\\gamma - 1} = 300 \\times 10^{0.4} \\approx 300 \\times 2.5119 \\approx 753.6\\,\\text{K}$$\\n2. Công nén nhận được:\\n$$|W| = n C_V (T_2 - T_1) = 1 \\times \\left(\\frac{5}{2} \\times 8.314\\right) \\times (753.6 - 300) = 20.785 \\times 453.6 \\approx 9428\\,\\text{J} \\approx 9.43\\,\\text{kJ}$$\\n(Đây chính là nguyên lý động cơ Diesel: nén không khí đến nhiệt độ cao để tự bốc cháy dầu phun vào!)."
        }
    ],
    "pitfalls": [
        {
            "error": "Quy ước dấu sai: nhầm giữa công sinh và công nhận",
            "fix": "Quy ước quốc tế: $W$ là công chất khí sinh ra ($W > 0$ khi dãn thể tích $V_2 > V_1$), khi đó $\\Delta U = Q - W$.",
            "tip": "Khí nở $\\to$ sinh công dương $\\to$ làm giảm nội năng nếu không cấp nhiệt."
        }
    ],
    "exercises": [
        {
            "id": "ex_12_1",
            "type": "easy",
            "q": "Một khối khí dãn đẳng áp ở áp suất không đổi $p = 2.0 \\times 10^5\\,\\text{Pa}$ từ thể tích $V_1 = 0.01\\,\\text{m}^3$ đến $V_2 = 0.03\\,\\text{m}^3$. Tính công do khí sinh ra (J).",
            "unit": "J",
            "ans": 4000.0,
            "tol": 10.0,
            "hints": ["$W = p(V_2 - V_1)$."],
            "solution": "$$W = 2.0 \\times 10^5 \\times (0.03 - 0.01) = 2.0 \\times 10^5 \\times 0.02 = 4000.0\\,\\text{J}$$\\nĐáp số: 4000.0 J"
        },
        {
            "id": "ex_12_2",
            "type": "easy",
            "q": "Một khối khí lý tưởng nhận nhiệt lượng $Q = 1500\\,\\text{J}$ trong một quá trình đẳng tích. Độ biến thiên nội năng $\\Delta U$ của khối khí là bao nhiêu Jun?",
            "unit": "J",
            "ans": 1500.0,
            "tol": 1.0,
            "hints": ["Quá trình đẳng tích $dV = 0 \\implies W = 0 \\implies \\Delta U = Q$."],
            "solution": "$$\\Delta U = Q = 1500.0\\,\\text{J}$$\\nĐáp số: 1500.0 J"
        },
        {
            "id": "ex_12_3",
            "type": "easy",
            "q": "Một mol khí lý tưởng dãn đẳng nhiệt ở $T = 300\\,\\text{K}$ từ $V_1 = 5.0\\,\\text{l}$ đến $V_2 = 10.0\\,\\text{l}$ ($R = 8.314$). Tính công do khí sinh ra theo Jun (làm tròn 1 chữ số).",
            "unit": "J",
            "ans": 1728.8,
            "tol": 5.0,
            "hints": ["$W = nRT \\ln(V_2/V_1)$."],
            "solution": "$$W = 1 \\times 8.314 \\times 300 \\times \\ln(2) \\approx 2494.2 \\times 0.69315 \\approx 1728.8\\,\\text{J}$$\\nĐáp số: 1728.8 J"
        },
        {
            "id": "ex_12_4",
            "type": "easy",
            "q": "Khí Oxy ($O_2$) là chất khí lưỡng nguyên tử cứng ($i = 5$). Chỉ số đoạn nhiệt $\\gamma$ của khí Oxy bằng bao nhiêu?",
            "unit": "",
            "ans": 1.4,
            "tol": 0.01,
            "hints": ["$\\gamma = \\frac{i+2}{i} = \\frac{7}{5}$."],
            "solution": "$$\\gamma = \\frac{7}{5} = 1.4$$\\nĐáp số: 1.4"
        },
        {
            "id": "ex_12_5",
            "type": "mid",
            "q": "Nén đoạn nhiệt 1 mol không khí ($\gamma = 1.4$) từ $T_1 = 300\\,\\text{K}$, thể tích giảm 10 lần. Tính nhiệt độ cuối $T_2$ theo Kelvin (làm tròn 1 chữ số).",
            "unit": "K",
            "ans": 753.6,
            "tol": 2.0,
            "hints": ["$T_2 = T_1 (10)^{\\gamma - 1} = 300 \\times 10^{0.4}$."],
            "solution": "$$T_2 = 300 \\times 10^{0.4} \\approx 300 \\times 2.5119 \\approx 753.6\\,\\text{K}$$\\nĐáp số: 753.6 K"
        },
        {
            "id": "ex_12_6",
            "type": "mid",
            "q": "Trong quá trình nén đoạn nhiệt ở câu trên ($T_1 = 300\\,\\text{K}, T_2 = 753.6\\,\\text{K}, C_V = 2.5R$), công mà khối khí nhận được bằng bao nhiêu kilôjun (kJ)?",
            "unit": "kJ",
            "ans": 9.43,
            "tol": 0.1,
            "hints": ["$|W| = n C_V (T_2 - T_1)$."],
            "solution": "$$|W| = 1 \\times (2.5 \\times 8.314) \\times (753.6 - 300) = 20.785 \\times 453.6 \\approx 9428\\,\\text{J} \\approx 9.43\\,\\text{kJ}$$\\nĐáp số: 9.43 kJ"
        },
        {
            "id": "ex_12_7",
            "type": "mid",
            "q": "Khí thực hiện một chu trình hình chữ nhật trên đồ thị p-V với $p_0 = 10^5\\,\\text{Pa}, V_0 = 0.02\\,\\text{m}^3$. Công của chu trình là $W = p_0 V_0$. Tính $W$ theo Jun.",
            "unit": "J",
            "ans": 2000.0,
            "tol": 10.0,
            "hints": ["$W = 10^5 \\times 0.02$."],
            "solution": "$$W = 100000 \\times 0.02 = 2000.0\\,\\text{J}$$\\nĐáp số: 2000.0 J"
        },
        {
            "id": "ex_12_8",
            "type": "mid",
            "q": "Khí đơn nguyên tử nhận nhiệt trong hai nhánh chu trình chữ nhật ở câu 7 với tổng nhiệt nhận $Q_1 = 6.5 p_0 V_0$. Tính hiệu suất $\\eta = W / Q_1$ theo phần trăm.",
            "unit": "%",
            "ans": 15.4,
            "tol": 0.2,
            "hints": ["$\\eta = 1 / 6.5 \\times 100\\%$."],
            "solution": "$$\\eta = \\frac{1}{6.5} \\times 100\\% \\approx 15.38\\% \\approx 15.4\\%$$\\nĐáp số: 15.4 %"
        },
        {
            "id": "ex_12_9",
            "type": "hard",
            "q": "Một khối khí đơn nguyên tử ($C_V = 1.5R$) thực hiện quá trình đa phương $p V^2 = \\text{const}$ ($m = 2$). Cho $R = 8.314$. Tính nhiệt dung mol của quá trình theo $\\text{J/(mol}\\cdot\\text{K)}$.",
            "unit": "J/(mol·K)",
            "ans": 4.16,
            "tol": 0.05,
            "hints": ["$C_m = C_V - \\frac{R}{m - 1} = 1.5R - R = 0.5R$."],
            "solution": "$$C_m = 0.5 \\times 8.314 = 4.157 \\approx 4.16\\,\\text{J/(mol}\\cdot\\text{K)}$$\\nĐáp số: 4.16"
        },
        {
            "id": "ex_12_10",
            "type": "hard",
            "q": "Khí lưỡng nguyên tử ($C_V = 2.5R$) thực hiện quá trình đa phương $p V^{-1} = \\text{const}$ ($m = -1$). Tính nhiệt dung mol $C_m$ của khối khí theo $\\text{J/(mol}\\cdot\\text{K)}$.",
            "unit": "J/(mol·K)",
            "ans": 24.94,
            "tol": 0.1,
            "hints": ["$C_m = 2.5R - \\frac{R}{-1 - 1} = 2.5R + 0.5R = 3.0R$."],
            "solution": "$$C_m = 3.0 \\times 8.314 = 24.942 \\approx 24.94\\,\\text{J/(mol}\\cdot\\text{K)}$$\\nĐáp số: 24.94"
        }
    ]
}

CH13 = {
    "id": 13,
    "num": 13,
    "part": "Phần III — Nhiệt học",
    "title": "Nguyên lý thứ hai và Entropy",
    "tag": "Chu trình Carnot, Clausius & Chiều hướng tự nhiên",
    "status": "ready",
    "summary": "Quá trình thuận nghịch và bất thuận nghịch, các phát biểu Kelvin-Planck và Clausius, chu trình Carnot và định lý Carnot, bất đẳng thức Clausius, hàm trạng thái Entropy, ý nghĩa thống kê Boltzmann (S = k ln Ω), chu trình động cơ thực tế.",
    "nature": {
        "why": "Nguyên lý I chỉ nói năng lượng bảo toàn nhưng không cho biết chiều diễn biến tự nhiên. Nguyên lý II xác định chiều một chiều không thể đảo ngược của thời gian và quá trình nhiệt vĩ mô.",
        "meaning": "Nhiệt không thể tự phát truyền từ vật lạnh sang vật nóng. Không thể chế tạo động cơ nhiệt chỉ nhận nhiệt từ một nguồn duy nhất mà biến hoàn toàn thành công (bác bỏ động cơ vĩnh cửu loại 2). Entropy $S$ là thước đo mức độ hỗn loạn vi mô; trong hệ cô lập, entropy luôn luôn tăng hoặc không đổi.",
        "conditions": "Hệ nhiệt động kín tự do diễn biến; động cơ nhiệt hoạt động tuần hoàn giữa hai nguồn nhiệt.",
        "limits": "Nguyên lý II mang bản chất thống kê xác suất; với hệ cực nhỏ gồm vài phân tử trong thời gian cực ngắn, có thể xuất hiện thăng giáng vi mô vi phạm tạm thời."
    },
    "formulas": [
        {
            "name": "Chu trình Carnot và Hiệu suất Cực đại",
            "latex": "\\eta_C = 1 - \\frac{T_2}{T_1} = \\frac{Q_1 - Q_2}{Q_1}; \\quad \\frac{Q_1}{T_1} = \\frac{Q_2}{T_2}; \\quad \\varepsilon_C = \\frac{T_2}{T_1 - T_2}",
            "meaning": "Động cơ Carnot gồm 2 quá trình đẳng nhiệt và 2 quá trình đoạn nhiệt thuận nghịch. Hiệu suất chỉ phụ thuộc nhiệt độ hai nguồn nhiệt, độc lập với chất làm việc.",
            "proof": [
                {"step": "Q_1 = nRT_1\\ln\\left(\\frac{V_2}{V_1}\\right), \\quad Q_2 = nRT_2\\ln\\left(\\frac{V_3}{V_4}\\right)", "reason": "Nhiệt lượng trao đổi trong hai giai đoạn dãn và nén đẳng nhiệt"},
                {"step": "T_1 V_2^{\\gamma - 1} = T_2 V_3^{\\gamma - 1}, \\quad T_1 V_1^{\\gamma - 1} = T_2 V_4^{\\gamma - 1} \\implies \\frac{V_2}{V_1} = \\frac{V_3}{V_4}", "reason": "Chia hai phương trình đoạn nhiệt vế theo vế"},
                {"step": "\\frac{Q_2}{Q_1} = \\frac{T_2}{T_1} \\implies \\eta_C = 1 - \\frac{Q_2}{Q_1} = 1 - \\frac{T_2}{T_1}", "reason": "Hiệu suất động cơ Carnot"}
            ]
        },
        {
            "name": "Bất đẳng thức Clausius và Hàm trạng thái Entropy",
            "latex": "\\oint \\frac{\\delta Q}{T} \\le 0; \\quad dS = \\frac{\\delta Q_{tn}}{T}; \\quad \\Delta S_{cô\\,lập} \\ge 0; \\quad S = k \\ln\\Omega",
            "meaning": "Tích phân Clausius theo chu trình kín bằng 0 khi thuận nghịch và âm khi bất thuận nghịch. Trong hệ cô lập, entropy luôn tăng hướng tới trạng thái xác suất cực đại.",
            "proof": [
                {"step": "\\oint \\frac{\\delta Q_{tn}}{T} = 0 \\implies \\int_A^B \\frac{\\delta Q_{tn}}{T} \\text{ không phụ thuộc đường đi}", "reason": "Tích phân chu trình kín bằng 0 định nghĩa hàm trạng thái S"},
                {"step": "S_B - S_A = \\int_A^B \\frac{\\delta Q_{tn}}{T}", "reason": "Định nghĩa vi phân của Entropy dS = δQ_tn / T"},
                {"step": "\\delta Q = 0 \\implies dS \\ge 0 \\implies \\Delta S \\ge 0", "reason": "Nguyên lý tăng entropy đối với hệ cô lập"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Hiệu suất động cơ Carnot, nhiệt lượng và công suất",
            "algorithm": [
                "Bước 1: Tính hiệu suất Carnot: $\\eta = 1 - T_2 / T_1$ (chú ý đổi $T$ sang Kelvin).",
                "Bước 2: Sử dụng quan hệ công và nhiệt: $W = \\eta Q_1$, $Q_2 = Q_1(1 - \\eta) = Q_1 - W$.",
                "Bước 3: Với máy lạnh: Hệ số làm lạnh $\\varepsilon = \\frac{Q_2}{W} = \\frac{T_2}{T_1 - T_2}$."
            ]
        },
        {
            "name": "Dạng 2: Tính biến thiên Entropy trong các quá trình nhiệt động",
            "algorithm": [
                "Bước 1: Khí lý tưởng: $\\Delta S = n C_V \\ln(T_2/T_1) + nR\\ln(V_2/V_1) = n C_p \\ln(T_2/T_1) - nR\\ln(p_2/p_1)$.",
                "Bước 2: Chuyển pha ở $T$ không đổi: $\\Delta S = \\frac{m L}{T}$.",
                "Bước 3: Đun nóng chất lỏng/rắn: $\\Delta S = m c \\ln(T_2/T_1)$.",
                "Bước 4: Truyền nhiệt giữa hai nguồn: $\\Delta S = -\\frac{Q}{T_h} + \\frac{Q}{T_c} > 0$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Động cơ nhiệt Carnot",
            "problem": "Một động cơ nhiệt Carnot hoạt động giữa nguồn nóng $T_1 = 500\\,\\text{K}$ và nguồn lạnh $T_2 = 300\\,\\text{K}$. Trong mỗi chu trình, động cơ nhận nhiệt lượng $Q_1 = 2000\\,\\text{J}$ từ nguồn nóng. Tính hiệu suất $\\eta$, công sinh ra $W$ và nhiệt thải ra $Q_2$.",
            "analysis": "Áp dụng trực tiếp công thức Carnot: $\\eta = 1 - T_2/T_1$, $W = \\eta Q_1$, $Q_2 = Q_1 - W$.",
            "solution": "1. Hiệu suất động cơ Carnot:\\n$$\\eta = 1 - \\frac{T_2}{T_1} = 1 - \\frac{300}{500} = 1 - 0.6 = 0.40 = 40\\%$$\\n2. Công cơ học sinh ra trong 1 chu trình:\\n$$W = \\eta Q_1 = 0.40 \\times 2000 = 800\\,\\text{J}$$\\n3. Nhiệt lượng nhả cho nguồn lạnh:\\n$$Q_2 = Q_1 - W = 2000 - 800 = 1200\\,\\text{J}$$\\nĐáp số: η = 40%; W = 800 J; Q2 = 1200 J."
        }
    ],
    "pitfalls": [
        {
            "error": "Dùng nhiệt độ bách phân °C thay vì Kelvin trong công thức hiệu suất Carnot",
            "fix": "Công thức $\\eta = 1 - T_2/T_1$ CHỈ ĐÚNG khi nhiệt độ tính bằng thang Kelvin.",
            "tip": "Ví dụ nguồn nóng $100^\\circ\\text{C}$ và nguồn lạnh $0^\\circ\\text{C}$ thì $\\eta = 1 - 273/373 \\approx 26.8\\%$, chứ không phải $1 - 0/100 = 100\\%$!"
        }
    ],
    "exercises": [
        {
            "id": "ex_13_1",
            "type": "easy",
            "q": "Một động cơ nhiệt Carnot hoạt động giữa nguồn nóng $T_1 = 600\\,\\text{K}$ và nguồn lạnh $T_2 = 300\\,\\text{K}$. Tính hiệu suất của động cơ theo phần trăm.",
            "unit": "%",
            "ans": 50.0,
            "tol": 0.5,
            "hints": ["$\\eta = (1 - T_2/T_1) \\times 100\\%$."],
            "solution": "$$\\eta = \\left(1 - \\frac{300}{600}\\right) \\times 100\\% = 50.0\\%$$\\nĐáp số: 50.0 %"
        },
        {
            "id": "ex_13_2",
            "type": "easy",
            "q": "Động cơ Carnot nhận nhiệt từ nguồn nóng $Q_1 = 2000\\,\\text{J}$ với hiệu suất $\\eta = 40\\% = 0.4$. Nhiệt lượng mà động cơ thải ra cho nguồn lạnh bằng bao nhiêu Jun?",
            "unit": "J",
            "ans": 1200.0,
            "tol": 5.0,
            "hints": ["$Q_2 = Q_1(1 - \\eta)$."],
            "solution": "$$Q_2 = 2000 \\times (1 - 0.4) = 2000 \\times 0.6 = 1200.0\\,\\text{J}$$\\nĐáp số: 1200.0 J"
        },
        {
            "id": "ex_13_3",
            "type": "easy",
            "q": "Một máy lạnh Carnot hoạt động giữa ngăn đông $T_2 = 250\\,\\text{K}$ và nhiệt độ phòng $T_1 = 300\\,\\text{K}$. Tính hệ số làm lạnh $\\varepsilon_C$ của máy.",
            "unit": "",
            "ans": 5.0,
            "tol": 0.05,
            "hints": ["$\\varepsilon_C = \\frac{T_2}{T_1 - T_2}$."],
            "solution": "$$\\varepsilon_C = \\frac{250}{300 - 250} = \\frac{250}{50} = 5.0$$\\nĐáp số: 5.0"
        },
        {
            "id": "ex_13_4",
            "type": "easy",
            "q": "Khối lượng $m = 1.0\\,\\text{kg}$ nước đá tan ở nhiệt độ không đổi $T = 273\\,\\text{K}$. Ẩn nhiệt nóng chảy của nước đá là $\\lambda = 3.34 \\times 10^5\\,\\text{J/kg}$. Tính độ biến thiên entropy $\\Delta S$ theo J/K.",
            "unit": "J/K",
            "ans": 1223.4,
            "tol": 2.0,
            "hints": ["$\\Delta S = \\frac{m \\lambda}{T}$."],
            "solution": "$$\\Delta S = \\frac{1.0 \\times 3.34 \\times 10^5}{273} \\approx 1223.44 \\approx 1223.4\\,\\text{J/K}$$\\nĐáp số: 1223.4 J/K"
        },
        {
            "id": "ex_13_5",
            "type": "mid",
            "q": "Cho $n = 2\\,\\text{mol}$ khí lý tưởng dãn tự do vào chân không, thể tích tăng gấp đôi ($V_2 = 2V_1$). Cho $R = 8.314$. Tính độ biến thiên entropy $\\Delta S$ theo J/K.",
            "unit": "J/K",
            "ans": 11.5,
            "tol": 0.2,
            "hints": ["$\\Delta S = n R \\ln(V_2/V_1) = 2 \\times 8.314 \\times \\ln(2)$."],
            "solution": "$$\\Delta S = 2 \\times 8.314 \\times \\ln(2) \\approx 16.628 \\times 0.69315 \\approx 11.52 \\approx 11.5\\,\\text{J/K}$$\\nĐáp số: 11.5 J/K"
        },
        {
            "id": "ex_13_6",
            "type": "mid",
            "q": "Nhiệt lượng $Q = 6000\\,\\text{J}$ tự phát truyền qua vách dẫn nhiệt từ vật nóng $T_h = 600\\,\\text{K}$ sang vật lạnh $T_c = 300\\,\\text{K}$. Tính độ tăng entropy tổng cộng của hệ cô lập theo J/K.",
            "unit": "J/K",
            "ans": 10.0,
            "tol": 0.1,
            "hints": ["$\\Delta S = -\\frac{Q}{T_h} + \\frac{Q}{T_c}$."],
            "solution": "$$\\Delta S = -\\frac{6000}{600} + \\frac{6000}{300} = -10 + 20 = 10.0\\,\\text{J/K}$$\\nĐáp số: 10.0 J/K"
        },
        {
            "id": "ex_13_7",
            "type": "mid",
            "q": "Một chu trình Otto lý thuyết có tỉ số nén $r = 8$ và $\\gamma = 1.4$. Tính hiệu suất nhiệt $\\eta_{Otto} = 1 - 1/r^{\\gamma - 1}$ theo phần trăm (làm tròn 1 chữ số).",
            "unit": "%",
            "ans": 56.5,
            "tol": 0.2,
            "hints": ["$\\eta = (1 - 8^{-0.4}) \\times 100\\%$."],
            "solution": "$$\\eta = (1 - 8^{-0.4}) \\times 100\\% = (1 - 0.435275) \\times 100\\% \\approx 56.47\\% \\approx 56.5\\%$$\\nĐáp số: 56.5 %"
        },
        {
            "id": "ex_13_8",
            "type": "mid",
            "q": "Đun nóng $m = 2.0\\,\\text{kg}$ nước từ $T_1 = 293\\,\\text{K}$ lên $T_2 = 353\\,\\text{K}$ ($c = 4186\\,\\text{J/(kg}\\cdot\\text{K)}$). Tính độ biến thiên entropy $\\Delta S$ theo J/K.",
            "unit": "J/K",
            "ans": 1559.7,
            "tol": 2.0,
            "hints": ["$\\Delta S = m c \\ln(T_2/T_1)$."],
            "solution": "$$\\Delta S = 2.0 \\times 4186 \\times \\ln\\left(\\frac{353}{293}\\right) = 8372 \\times 0.1863 \\approx 1559.7\\,\\text{J/K}$$\\nĐáp số: 1559.7 J/K"
        },
        {
            "id": "ex_13_9",
            "type": "hard",
            "q": "Trộn $m = 1.0\\,\\text{kg}$ nước ở $T_1 = 300\\,\\text{K}$ với $m = 1.0\\,\\text{kg}$ nước ở $T_2 = 360\\,\\text{K}$ trong bình cách nhiệt ($c = 4186\\,\\text{J/(kg}\\cdot\\text{K)}$). Tính độ tăng entropy của hệ sau khi cân bằng theo J/K.",
            "unit": "J/K",
            "ans": 34.7,
            "tol": 0.5,
            "hints": ["$T_f = 330\\,\\text{K}$.", "$\\Delta S = m c \\ln\\left(\\frac{T_f^2}{T_1 T_2}\\right)$."],
            "solution": "$$\\Delta S = 1.0 \\times 4186 \\times \\ln\\left(\\frac{330^2}{300 \\times 360}\\right) = 4186 \\times \\ln(1.008333) \\approx 34.74 \\approx 34.7\\,\\text{J/K}$$\\nĐáp số: 34.7 J/K"
        },
        {
            "id": "ex_13_10",
            "type": "hard",
            "q": "Hệ có 1 mol khí lý tưởng dãn thể tích gấp đôi ($V_2 = 2V_1$). Theo công thức thống kê Boltzmann, số vi trạng thái tăng tỉ lệ $\\Omega_2 / \\Omega_1 = 2^{N_A}$. Với $R = 8.314$, tính độ tăng entropy $\\Delta S = k \\ln(\\Omega_2/\\Omega_1)$ theo J/K.",
            "unit": "J/K",
            "ans": 5.76,
            "tol": 0.05,
            "hints": ["$\\Delta S = R \\ln(2)$."],
            "solution": "$$\\Delta S = 8.314 \\times \\ln(2) = 8.314 \\times 0.69315 \\approx 5.763 \\approx 5.76\\,\\text{J/K}$$\\nĐáp số: 5.76 J/K"
        }
    ]
}

CH14 = {
    "id": 14,
    "num": 14,
    "part": "Phần III — Nhiệt học",
    "title": "Khí thực và Chuyển pha",
    "tag": "Phương trình Van der Waals & Chuyển pha loại 1",
    "status": "ready",
    "summary": "Mô hình khí thực, phương trình Van der Waals, các thông số tại điểm tới hạn (Tc, pc, Vc), chuyển pha loại 1 và phương trình Clapeyron-Clausius, độ ẩm không khí, hiệu ứng Joule-Thomson.",
    "nature": {
        "why": "Khí lý tưởng không giải thích được hiện tượng ngưng tụ khí thành lỏng và sự tồn tại của trạng thái tới hạn.",
        "meaning": "Phương trình Van der Waals đưa vào hai số hiệu chỉnh: $a/V_m^2$ bù đắp lực hút giữa các phân tử (áp suất nội), và $b$ bù đắp thể tích riêng bị loại trừ do các phân tử chiếm chỗ. Trên nhiệt độ tới hạn $T_c$, không thể hóa lỏng khí bằng cách nén đẳng nhiệt.",
        "conditions": "Áp dụng cho khí thực ở áp suất trung bình và nhiệt độ không quá xa điểm bão hòa.",
        "limits": "Khi áp suất cực cao, hằng số a và b phụ thuộc vào mật độ và nhiệt độ, cần phương trình trạng thái phức tạp hơn như Redlich-Kwong."
    },
    "formulas": [
        {
            "name": "Phương trình Trạng thái Van der Waals",
            "latex": "\\left(p + \\frac{a}{V_m^2}\\right)(V_m - b) = RT; \\quad \\left(p + \\frac{an^2}{V^2}\\right)(V - nb) = nRT",
            "meaning": "$b \\approx 4 N_A \\frac{4}{3}\\pi r^3$ là thể tích loại trừ của 1 mol phân tử. $a/V_m^2$ là áp suất nội kéo phân tử vào trong.",
            "proof": [
                {"step": "p_{thực} = p_{lý\\,tưởng} - p_{nội} \\implies p_{lý\\,tưởng} = p + \\frac{a}{V_m^2}", "reason": "Lực hút phân tử ở lớp bề mặt làm giảm áp lực ép lên thành bình"},
                {"step": "V_{tự\\,do} = V_m - b", "reason": "Các phân tử không thể xuyên qua nhau, thể tích chuyển động tự do bị giảm đi"},
                {"step": "p_{lý\\,tưởng} V_{tự\\,do} = RT \\implies \\left(p + \\frac{a}{V_m^2}\\right)(V_m - b) = RT", "reason": "Thay vào phương trình khí lý tưởng thu được phương trình Van der Waals"}
            ]
        },
        {
            "name": "Các Thông số tại Điểm Tới hạn và Trạng thái Tương ứng",
            "latex": "V_{mc} = 3b; \\quad p_c = \\frac{a}{27b^2}; \\quad T_c = \\frac{8a}{27Rb}; \\quad \\frac{p_c V_{mc}}{R T_c} = \\frac{3}{8}",
            "meaning": "Tại điểm tới hạn, đường đẳng nhiệt có điểm uốn nằm ngang: $\\left(\\frac{\\partial p}{\\partial V}\\right)_T = 0$ và $\\left(\\frac{\\partial^2 p}{\\partial V^2}\\right)_T = 0$. Ranh giới giữa lỏng và khí biến mất.",
            "proof": [
                {"step": "p = \\frac{RT}{V_m - b} - \\frac{a}{V_m^2}", "reason": "Biểu diễn áp suất p theo thể tích mol Vm"},
                {"step": "\\frac{\\partial p}{\\partial V_m} = -\\frac{RT}{(V_m - b)^2} + \\frac{2a}{V_m^3} = 0, \\quad \\frac{\\partial^2 p}{\\partial V_m^2} = \\frac{2RT}{(V_m - b)^3} - \\frac{6a}{V_m^4} = 0", "reason": "Điều kiện điểm uốn nằm ngang tại nhiệt độ tới hạn Tc"},
                {"step": "\\frac{2}{V_m - b} = \\frac{3}{V_m} \\implies 2V_m = 3V_m - 3b \\implies V_{mc} = 3b", "reason": "Chia hai phương trình đạo hàm vế theo vế"},
                {"step": "T_c = \\frac{8a}{27Rb}, \\quad p_c = \\frac{a}{27b^2}", "reason": "Thế V_mc = 3b vào hai phương trình để giải tìm Tc và pc"}
            ]
        },
        {
            "name": "Chuyển pha loại 1 và Phương trình Clapeyron - Clausius",
            "latex": "\\frac{dp}{dT} = \\frac{L}{T(V_2 - V_1)}; \\quad \\ln\\left(\\frac{p}{p_0}\\right) = -\\frac{L}{R}\\left(\\frac{1}{T} - \\frac{1}{T_0}\\right)",
            "meaning": "Mô tả sự phụ thuộc của áp suất bão hòa (nhiệt độ sôi, nhiệt độ nóng chảy) vào nhiệt độ. $L$ là ẩn nhiệt chuyển pha.",
            "proof": [
                {"step": "W = \\Delta p (V_2 - V_1)", "reason": "Công của chu trình Carnot vi mô giữa hai đường đẳng nhiệt lân cận"},
                {"step": "\\eta = \\frac{W}{Q_1} = \\frac{\\Delta p(V_2 - V_1)}{L} = \\frac{dT}{T}", "reason": "Đồng nhất với hiệu suất chu trình Carnot thuận nghịch"},
                {"step": "\\frac{dp}{dT} = \\frac{L}{T(V_2 - V_1)}", "reason": "Phương trình Clapeyron-Clausius"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Tính các thông số tới hạn của khí Van der Waals",
            "algorithm": [
                "Bước 1: Áp dụng $V_{mc} = 3b$, $p_c = \\frac{a}{27b^2}$, $T_c = \\frac{8a}{27Rb}$.",
                "Bước 2: Hệ số nén tới hạn bất biến: $Z_c = \\frac{p_c V_{mc}}{R T_c} = \\frac{3}{8} = 0.375$.",
                "Bước 3: Nhiệt độ nghịch đảo Joule-Thomson cực đại: $T_i = \\frac{2a}{Rb}$."
            ]
        },
        {
            "name": "Dạng 2: Ứng dụng phương trình Clapeyron-Clausius cho nhiệt độ sôi",
            "algorithm": [
                "Bước 1: Viết phương trình tích phân: $\\ln(p / p_0) = -\\frac{L_m}{R}(\\frac{1}{T} - \\frac{1}{T_0})$.",
                "Bước 2: Thay áp suất $p$ tại độ cao và tìm nhiệt độ sôi $T$.",
                "Bước 3: Đổi từ Kelvin sang độ C: $t = T - 273.15$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Tính nhiệt độ sôi của nước trên đỉnh núi cao",
            "problem": "Nước có ẩn nhiệt hóa hơi $L_m = 40.7\\,\\text{kJ/mol} = 40700\\,\\text{J/mol}$, sôi ở $373\\,\\text{K}$ khi áp suất $p_0 = 1\\,\\text{atm}$. Ở trên đỉnh núi nơi áp suất khí quyển chỉ còn $p = 0.7\\,\\text{atm}$, tính nhiệt độ sôi của nước theo °C.",
            "analysis": "Áp dụng phương trình Clapeyron-Clausius dạng tích phân: $\\ln(p/p_0) = -\\frac{L_m}{R}(1/T - 1/T_0)$.",
            "solution": "1. Lập phương trình:\\n$$\\ln(0.7) = -\\frac{40700}{8.314}\\left(\\frac{1}{T} - \\frac{1}{373}\\right)$$\\n$$-0.35667 = -4895.36 \\left(\\frac{1}{T} - 0.0026810\\right)$$\\n$$\\frac{1}{T} - 0.0026810 = \\frac{-0.35667}{-4895.36} \\approx 0.00007286$$\\n$$\\frac{1}{T} = 0.00275386 \\implies T \\approx 363.13\\,\\text{K}$$\\n2. Đổi sang độ C:\\n$$t = 363.13 - 273.15 \\approx 89.98^\\circ\\text{C} \\approx 90.0^\\circ\\text{C}$$\\nĐáp số: Nhiệt độ sôi là 90.0 °C."
        }
    ],
    "pitfalls": [
        {
            "error": "Cho rằng khí luôn có thể hóa lỏng bằng cách tăng áp suất ở bất kỳ nhiệt độ nào",
            "fix": "Nếu nhiệt độ của khí cao hơn nhiệt độ tới hạn ($T > T_c$), dù tăng áp suất lên hàng nghìn atm khí vẫn không bao giờ hóa lỏng mà chỉ chuyển thành chất lưu siêu tới hạn.",
            "tip": "Muốn hóa lỏng một chất khí, bước đầu tiên bắt buộc phải làm lạnh nó xuống dưới nhiệt độ tới hạn $T_c$."
        }
    ],
    "exercises": [
        {
            "id": "ex_14_1",
            "type": "easy",
            "q": "Một chất khí có hằng số Van der Waals $b = 4.0 \\times 10^{-5}\\,\\text{m}^3/\\text{mol}$. Với $n = 2.0\\,\\text{mol}$ khí, thể tích riêng mà các phân tử chiếm chỗ là bao nhiêu lít?",
            "unit": "lít",
            "ans": 0.08,
            "tol": 0.005,
            "hints": ["$V_b = n b$. Đổi $\\text{m}^3$ sang lít nhân với 1000."],
            "solution": "$$V_b = 2.0 \\times (4.0 \\times 10^{-5}) \\times 1000 = 0.08\\,\\text{lít}$$\\nĐáp số: 0.08 lít"
        },
        {
            "id": "ex_14_2",
            "type": "easy",
            "q": "Cho $a = 0.36\\,\\text{Pa}\\cdot\\text{m}^6/\\text{mol}^2$. Khi thể tích mol là $V_m = 0.002\\,\\text{m}^3/\\text{mol}$, áp suất nội tại $p_i = a/V_m^2$ bằng bao nhiêu kPa?",
            "unit": "kPa",
            "ans": 90.0,
            "tol": 0.5,
            "hints": ["$p_i = \\frac{0.36}{0.002^2}$, đổi sang kPa."],
            "solution": "$$p_i = \\frac{0.36}{4 \\times 10^{-6}} = 90000\\,\\text{Pa} = 90.0\\,\\text{kPa}$$\\nĐáp số: 90.0 kPa"
        },
        {
            "id": "ex_14_3",
            "type": "easy",
            "q": "Cho hằng số Van der Waals $b = 3.6 \\times 10^{-5}\\,\\text{m}^3/\\text{mol}$. Thể tích mol của chất khí tại điểm tới hạn $V_{mc} = 3b$ bằng bao nhiêu lít/mol?",
            "unit": "lít/mol",
            "ans": 0.108,
            "tol": 0.005,
            "hints": ["$V_{mc} = 3 \\times 3.6 \\times 10^{-5}\\,\\text{m}^3 = 1.08 \\times 10^{-4}\\,\\text{m}^3 = 0.108\\,\\text{lít}$."],
            "solution": "$$V_{mc} = 3 \\times (3.6 \\times 10^{-5}) \\times 1000 = 0.108\\,\\text{lít/mol}$$\\nĐáp số: 0.108 lít/mol"
        },
        {
            "id": "ex_14_4",
            "type": "easy",
            "q": "Theo phương trình Van der Waals, tỉ số nén tại điểm tới hạn $Z_c = \\frac{p_c V_{mc}}{R T_c}$ bằng bao nhiêu dạng số thập phân?",
            "unit": "",
            "ans": 0.375,
            "tol": 0.005,
            "hints": ["$Z_c = 3/8 = 0.375$."],
            "solution": "$$Z_c = \\frac{3}{8} = 0.375$$\\nĐáp số: 0.375"
        },
        {
            "id": "ex_14_5",
            "type": "mid",
            "q": "Một chất khí có $a = 0.136\\,\\text{Pa}\\cdot\\text{m}^6/\\text{mol}^2, b = 3.2 \\times 10^{-5}\\,\\text{m}^3/\\text{mol}, R = 8.314$. Tính nhiệt độ tới hạn $T_c$ của chất khí theo Kelvin (làm tròn 1 chữ số).",
            "unit": "K",
            "ans": 151.5,
            "tol": 0.5,
            "hints": ["$T_c = \\frac{8a}{27Rb}$."],
            "solution": "$$T_c = \\frac{8 \\times 0.136}{27 \\times 8.314 \\times 3.2 \\times 10^{-5}} = \\frac{1.088}{0.0071833} \\approx 151.46 \\approx 151.5\\,\\text{K}$$\\nĐáp số: 151.5 K"
        },
        {
            "id": "ex_14_6",
            "type": "mid",
            "q": "Với dữ kiện khí ở câu trên, hãy tính áp suất tới hạn $p_c$ theo đơn vị Megapascal (MPa, làm tròn 2 chữ số).",
            "unit": "MPa",
            "ans": 4.92,
            "tol": 0.05,
            "hints": ["$p_c = \\frac{a}{27b^2}$."],
            "solution": "$$p_c = \\frac{0.136}{27 \\times (3.2 \\times 10^{-5})^2} = \\frac{0.136}{2.7648 \\times 10^{-8}} \\approx 4919000\\,\\text{Pa} \\approx 4.92\\,\\text{MPa}$$\\nĐáp số: 4.92 MPa"
        },
        {
            "id": "ex_14_7",
            "type": "mid",
            "q": "Nước có ẩn nhiệt hóa hơi $L_m = 40700\\,\\text{J/mol}$, sôi ở $373\\,\\text{K}$ tại áp suất $1\\,\\text{atm}$. Tại đỉnh núi có áp suất $0.7\\,\\text{atm}$, nhiệt độ sôi của nước bằng bao nhiêu °C? (Làm tròn 1 chữ số).",
            "unit": "°C",
            "ans": 90.0,
            "tol": 0.5,
            "hints": ["$\\ln(0.7) = -\\frac{40700}{8.314}(1/T - 1/373)$. Đổi $T$ sang $^\circ\\text{C}$."],
            "solution": "$$T \\approx 363.13\\,\\text{K} \\implies t = 363.13 - 273.15 \\approx 90.0^\\circ\\text{C}$$\\nĐáp số: 90.0 °C"
        },
        {
            "id": "ex_14_8",
            "type": "mid",
            "q": "Ở nhiệt độ $25^\\circ\\text{C}$, áp suất hơi nước bão hòa là $p_s = 3.17\\,\\text{kPa}$. Độ ẩm tương đối đo được là $\\phi = 75\\%$. Áp suất riêng phần của hơi nước trong không khí là bao nhiêu kPa?",
            "unit": "kPa",
            "ans": 2.38,
            "tol": 0.05,
            "hints": ["$p_{hơi} = \\phi \\times p_s = 0.75 \\times 3.17$."],
            "solution": "$$p_{hơi} = 0.75 \\times 3.17 \\approx 2.3775 \\approx 2.38\\,\\text{kPa}$$\\nĐáp số: 2.38 kPa"
        },
        {
            "id": "ex_14_9",
            "type": "hard",
            "q": "Theo định luật trạng thái tương ứng rút gọn $(\\pi + 3/\\phi^2)(3\\phi - 1) = 8\\tau$. Tại trạng thái có áp suất rút gọn $\\pi = 2.0$ và nhiệt độ rút gọn $\\tau = 1.25$, thể tích mol rút gọn $\\phi = V_m/V_{mc}$ bằng bao nhiêu?",
            "unit": "",
            "ans": 1.0,
            "tol": 0.05,
            "hints": ["Thay $\\pi = 2.0$ và $\\tau = 1.25$ ($8\\tau = 10$). Phương trình có nghiệm nguyên dương $\\phi = 1.0$."],
            "solution": "$$(2 + 3/\\phi^2)(3\\phi - 1) = 10 \\implies 2\\phi^3 - 4\\phi^2 + 3\\phi - 1 = 0 \\implies (\\phi - 1)(2\\phi^2 - 2\\phi + 1) = 0 \\implies \\phi = 1.0$$\\nĐáp số: 1.0"
        },
        {
            "id": "ex_14_10",
            "type": "hard",
            "q": "Nhiệt độ nghịch đảo cực đại của hiệu ứng Joule-Thomson đối với khí Van der Waals là $T_i = \\frac{2a}{Rb}$. Với $a = 0.136, b = 3.2 \\times 10^{-5}, R = 8.314$, tính $T_i$ theo Kelvin (làm tròn số nguyên).",
            "unit": "K",
            "ans": 1022.0,
            "tol": 2.0,
            "hints": ["$T_i = \\frac{2 \\times 0.136}{8.314 \\times 3.2 \\times 10^{-5}}$."],
            "solution": "$$T_i = \\frac{0.272}{0.00026605} \\approx 1022.37 \\approx 1022.0\\,\\text{K}$$\\nĐáp số: 1022.0 K"
        }
    ]
}

print("Chapters 11, 12, 13, 14 data module ready.")
