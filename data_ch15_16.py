# -*- coding: utf-8 -*-
"""
Module defining Chapter 15 & Chapter 16 for Vật lý đại cương 1
Toàn bộ dữ liệu được tính toán và kiểm chứng toán học bằng Python.
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf.
Định dạng dữ liệu chuẩn 100% tương thích với build_html.py.
"""

CH15 = {
    "id": 15,
    "num": 15,
    "part": "Phần IV — Bảng tổng kết & Phương pháp",
    "title": "Bảng công thức tổng hợp toàn diện",
    "tag": "Tra cứu nhanh & Tương tự Cơ - Nhiệt",
    "status": "ready",
    "summary": "Bảng tra cứu toàn diện các công thức cốt lõi của 14 chương Vật lý đại cương 1: Cơ học cổ điển, Dao động & Sóng, Nhiệt động lực học, hệ thống hằng số vật lý chuẩn SI và các cặp đại lượng tương tự (đối ngẫu tịnh tiến — quay).",
    "nature": {
        "why": "Vật lý học không phải là một tập hợp các công thức rời rạc mà là một cấu trúc thống nhất dựa trên các nguyên lý đối xứng và định luật bảo toàn (Định lý Noether). Việc tổng hợp và đối chiếu giúp nhận diện bản chất tương tự giữa các hiện tượng khác nhau.",
        "meaning": "Cung cấp cái nhìn toàn cảnh: Chuyển động quay tương đương với chuyển động tịnh tiến dưới sự thay thế tọa độ góc và momen quán tính; Năng lượng cơ học và nội nhiệt liên kết chặt chẽ qua định luật I nhiệt động lực học; Dao động và sóng liên hệ qua sự lan truyền pha trong không - thời gian.",
        "conditions": "Tra cứu công thức luôn phải đi kèm với điều kiện biên và phạm vi áp dụng (ví dụ: cơ học Newton chỉ đúng khi v << c, khí lý tưởng chỉ đúng ở áp suất thấp).",
        "limits": "Thuộc lòng công thức mà không hiểu điều kiện áp dụng sẽ dẫn đến việc áp dụng sai mô hình (như dùng công thức Carnot cho chu trình thực tế, dùng định luật bảo toàn cơ năng khi có ma sát)."
    },
    "formulas": [
        {
            "name": "Bảng đối chiếu Động lực học Tịnh tiến và Quay",
            "latex": "\\begin{aligned} x \\longleftrightarrow \\theta; \\quad v = \\frac{dx}{dt} \\longleftrightarrow \\omega = \\frac{d\\theta}{dt}; \\quad a = \\frac{dv}{dt} \\longleftrightarrow \\beta = \\frac{d\\omega}{dt} \\\\ m \\longleftrightarrow I; \\quad \\vec{F} = m\\vec{a} \\longleftrightarrow M = I\\beta; \\quad p = mv \\longleftrightarrow L = I\\omega \\\\ dW = \\vec{F}\\cdot d\\vec{r} \\longleftrightarrow dW = M d\\theta; \\quad K = \\frac{1}{2}mv^2 \\longleftrightarrow K_q = \\frac{1}{2}I\\omega^2 \\end{aligned}",
            "meaning": "Sự đối ngẫu toán học hoàn hảo giữa các đại lượng tịnh tiến dọc một trục và chuyển động quay quanh trục cố định.",
            "proof": [
                {"step": "dW_q = \\vec{F}\\cdot d\\vec{s} = (F_t)(R d\\theta) = (R F_t) d\\theta", "reason": "Độ dịch chuyển vi phân cung tròn ds = R dθ"},
                {"step": "M = R F_t \\implies dW_q = M d\\theta", "reason": "Định nghĩa momen của lực đối với trục quay"},
                {"step": "dW_q = (I\\beta) d\\theta = I \\frac{d\\omega}{dt} d\\theta = I \\omega d\\omega", "reason": "Thay M = Iβ và dθ/dt = ω"},
                {"step": "W_q = \\int_{\\omega_1}^{\\omega_2} I \\omega d\\omega = \\frac{1}{2}I\\omega_2^2 - \\frac{1}{2}I\\omega_1^2 = \\Delta K_q", "reason": "Tích phân hai vế cho định lý động năng quay"}
            ]
        },
        {
            "name": "Các định luật bảo toàn nền tảng",
            "latex": "\\sum \\vec{p} = \\text{const} \\; (\\sum \\vec{F}_{ng} = 0); \\quad \\sum \\vec{L} = \\text{const} \\; (\\sum \\vec{M}_{ng} = 0); \\quad E_c = K + U = \\text{const} \\; (\\text{lực thế})",
            "meaning": "Ba định luật bảo toàn xuất phát từ tính đối xứng của không gian và thời gian: Tính đồng nhất của thời gian sinh ra bảo toàn năng lượng, tính đồng nhất của không gian sinh ra bảo toàn động lượng, tính đẳng hướng của không gian sinh ra bảo toàn momen động lượng (Định lý Noether).",
            "proof": [
                {"step": "\\frac{d\\vec{P}}{dt} = \\sum \\vec{F}_{ng} = 0 \\implies \\vec{P} = \\text{const}", "reason": "Đạo hàm theo thời gian bằng 0 khi tổng ngoại lực triệt tiêu"},
                {"step": "\\frac{d\\vec{L}}{dt} = \\sum \\vec{M}_{ng} = 0 \\implies \\vec{L} = \\text{const}", "reason": "Đạo hàm theo thời gian bằng 0 khi tổng momen ngoại lực triệt tiêu"},
                {"step": "\\Delta K = W_{the} = -\\Delta U \\implies \\Delta(K + U) = 0", "reason": "Công của lực thế bằng độ giảm thế năng"}
            ]
        },
        {
            "name": "Hệ thống hằng số vật lý tiêu chuẩn SI",
            "latex": "g = 9.81\\,\\text{m/s}^2; \\; G = 6.674 \\times 10^{-11}\\,\\text{N}\\cdot\\text{m}^2/\\text{kg}^2; \\; c = 3.0 \\times 10^8\\,\\text{m/s}; \\; R = 8.314\\,\\text{J/(mol}\\cdot\\text{K)}; \\; N_A = 6.022 \\times 10^{23}; \\; k_B = 1.38 \\times 10^{-23}\\,\\text{J/K}",
            "meaning": "Các hằng số cơ bản chi phối toàn bộ vũ trụ từ vi mô hạt phân tử đến vĩ mô thiên hà.",
            "proof": [
                {"step": "k_B = \\frac{R}{N_A} = \\frac{8.314}{6.022 \\times 10^{23}} \\approx 1.3806 \\times 10^{-23}\\,\\text{J/K}", "reason": "Mối liên hệ giữa hằng số khí lý tưởng và hằng số Boltzmann trên mỗi phân tử"},
                {"step": "p_0 = 1\\,\\text{atm} = 101325\\,\\text{Pa} = 760\\,\\text{mmHg}", "reason": "Quy đổi áp suất tiêu chuẩn ở mực nước biển"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Phân tích thứ nguyên và kiểm tra tính đúng đắn của công thức (Dimensional Analysis)",
            "algorithm": [
                "Bước 1: Viết thứ nguyên của các đại lượng cơ sở trong hệ SI: Chiều dài $[L]$, Khối lượng $[M]$, Thời gian $[T]$, Nhiệt độ $[\\Theta]$.",
                "Bước 2: Phân tích thứ nguyên của vế trái $[VT]$ và vế phải $[VP]$.",
                "Bước 3: So sánh: Hai vế của một phương trình vật lý bắt buộc phải có cùng thứ nguyên. Các số hạng trong một tổng phải đồng thứ nguyên.",
                "Bước 4: Kiểm tra tính không thứ nguyên của đối số hàm siêu việt: hàm mũ ($e^x$), logarit ($\\ln x$), lượng giác ($\\sin x$) thì $x$ phải có thứ nguyên bằng 1."
            ]
        },
        {
            "name": "Dạng 2: Vận dụng tính tương tự đối ngẫu để giải bài toán cơ học quay",
            "algorithm": [
                "Bước 1: Chuyển đổi các đại lượng đề bài từ tịnh tiến ($m, v, a, s, F$) sang các đại lượng quay ($I, \\omega, \\beta, \\theta, M$).",
                "Bước 2: Sử dụng các phương trình tương đương: $\\omega = \\omega_0 + \\beta t$, $\\omega^2 - \\omega_0^2 = 2\\beta\\theta$, $W_q = M\\theta = \\Delta K_q$.",
                "Bước 3: Thay số và kiểm tra đơn vị: $\\omega$ (rad/s), $\\beta$ (rad/s$^2$), $I$ (kg$\\cdot$m$^2$), $M$ (N$\\cdot$m)."
            ]
        },
        {
            "name": "Dạng 3: Bài toán bảo toàn liên chương: Cơ học kết hợp Nhiệt động lực học",
            "algorithm": [
                "Bước 1: Nhận diện hiện tượng va chạm mềm, phanh hãm ma sát hoặc chuyển động trong chất khí: Cơ năng vĩ mô biến mất biến thành nội năng vi mô: $Q = -\\Delta E_c$.",
                "Bước 2: Viết phương trình bảo toàn năng lượng toàn phần: $K_{dau} + U_{dau} = K_{cuoi} + U_{cuoi} + Q_{toa}$.",
                "Bước 3: Dùng phương trình nhiệt lượng $Q = m c \\Delta T$ hoặc nguyên lý I nhiệt động học $Q = \\Delta U + W$ để tìm độ tăng nhiệt độ hoặc biến thiên trạng thái."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Tìm công thức chu kỳ con lắc vật lý bằng phân tích thứ nguyên",
            "problem": "Giả sử chu kỳ dao động nhỏ $T$ của con lắc vật lý phụ thuộc vào momen quán tính $I$, khối lượng $m$, gia tốc trọng trường $g$ và khoảng cách từ trục quay đến khối tâm $d$ theo dạng $T = C I^x m^y g^z d^w$ ($C$ là hằng số không thứ nguyên). Xác định mối quan hệ giữa các số mũ.",
            "analysis": "Phân tích thứ nguyên các đại lượng theo hệ SI: $[T]=T$, $[I]=M L^2$, $[m]=M$, $[g]=L T^{-2}$, $[d]=L$. Đồng nhất số mũ của $M, L, T$ ở hai vế.",
            "solution": "1. Viết phương trình thứ nguyên:\\n   $T^1 = (M L^2)^x (M)^y (L T^{-2})^z (L)^w = M^{x+y} L^{2x+z+w} T^{-2z}$.\\n2. Đồng nhất số mũ của hai vế:\\n   Số mũ của $T$: $1 = -2z \\implies z = -1/2$.\\n   Số mũ của $M$: $0 = x + y \\implies y = -x$.\\n   Số mũ của $L$: $0 = 2x + z + w = 2x - 1/2 + w \\implies w = 1/2 - 2x$.\\n3. Vì dao động phụ thuộc trực tiếp vào tỉ số quán tính $I/(m d^2)$, ta có $x = 1/2, y = -1/2, w = -1/2$. Do đó:\\n   $T = C \\sqrt{\\frac{I}{m g d}}$ — hoàn toàn trùng khớp với công thức giải tích chính xác từ phương trình vi phân dao động!"
        }
    ],
    "pitfalls": [
        {
            "error": "Nhầm lẫn khi đổi đơn vị nhiệt độ trong phương trình trạng thái khí",
            "fix": "Trong các công thức $pV = nRT$ và $\\Delta S = \\int dQ/T$, nhiệt độ BẮT BUỘC phải đổi sang Kelvin: $T(\\text{K}) = t(^\\circ\\text{C}) + 273.15$.",
            "tip": "Chỉ khi tính độ biến thiên $\\Delta T = T_2 - T_1$ thì độ chênh theo $^\\circ\\text{C}$ mới bằng độ chênh theo K."
        },
        {
            "error": "Quên đổi đơn vị áp suất và thể tích sang hệ SI chuẩn khi tính công",
            "fix": "Đổi $1\\,\\text{atm} = 101325\\,\\text{Pa}$, $1\\,\\text{bar} = 10^5\\,\\text{Pa}$, $1\\,\\text{lít} = 10^{-3}\\,\\text{m}^3$.",
            "tip": "Công có đơn vị Joule khi $p$ có đơn vị Pa (N/m$^2$) và $V$ có đơn vị m$^3$. Nếu để l·atm thì $1\\,\\text{l}\\cdot\\text{atm} = 101.325\\,\\text{J}$."
        },
        {
            "error": "Quên động năng quay khi vật vừa tịnh tiến vừa quay (lăn không trượt)",
            "fix": "Tổng động năng phải là $K = \\frac{1}{2}mv_c^2 + \\frac{1}{2}I_c\\omega^2$.",
            "tip": "Với khối trụ đặc $I = \\frac{1}{2}mR^2$, động năng quay chiếm $1/3$ và tịnh tiến chiếm $2/3$ tổng động năng."
        }
    ],
    "exercises": [
        {
            "id": "ch15_ex1",
            "type": "easy",
            "q": "Áp suất của một bình chứa khí là $p = 2.5\\,\\text{atm}$. Tính giá trị của áp suất này theo đơn vị kilopascal ($\\text{kPa}$), biết $1\\,\\text{atm} = 101325\\,\\text{Pa}$.",
            "unit": "kPa",
            "ans": 253.31,
            "tol": 0.5,
            "hints": ["Đổi trực tiếp: $p(\\text{kPa}) = 2.5 \\times 101.325\\,\\text{kPa}$."],
            "solution": "$p = 2.5 \\times 101325\\,\\text{Pa} = 253312.5\\,\\text{Pa} \\approx 253.31\\,\\text{kPa}$."
        },
        {
            "id": "ch15_ex2",
            "type": "easy",
            "q": "Một electron ($m_0 = 9.11 \\times 10^{-31}\\,\\text{kg}$) chuyển động với tốc độ $v = 0.8c$ ($c = 3 \\times 10^8\\,\\text{m/s}$). Tính động lượng tương đối tính $p$ của electron theo đơn vị $10^{-22}\\,\\text{kg}\\cdot\\text{m/s}$.",
            "unit": "10^-22 kg.m/s",
            "ans": 3.64,
            "tol": 0.05,
            "hints": ["Áp dụng hệ thức Lorentz: $\\gamma = 1/\\sqrt{1 - (v/c)^2} = 1/0.6 \\approx 1.667$. Động lượng $p = \\gamma m_0 v$."],
            "solution": "1. Hệ số Lorentz: $\\gamma = 1/\\sqrt{1 - 0.8^2} = 1/0.6 = 5/3 \\approx 1.6667$.\\n2. Động lượng: $p = \\gamma m_0 v = \\frac{5}{3} \\times 9.11 \\times 10^{-31} \\times (0.8 \\times 3 \\times 10^8) = 3.644 \\times 10^{-22}\\,\\text{kg}\\cdot\\text{m/s}$."
        },
        {
            "id": "ch15_ex3",
            "type": "easy",
            "q": "Một khối trụ tròn đặc đồng chất lăn không trượt trên mặt phẳng ngang. Tính phần trăm (%) động năng quay chiếm trong tổng động năng của khối trụ.",
            "unit": "%",
            "ans": 33.33,
            "tol": 0.5,
            "hints": ["Khối trụ đặc có $I = \\frac{1}{2}mR^2$. Điều kiện lăn không trượt: $v = \\omega R$. So sánh $K_q = \\frac{1}{2}I\\omega^2$ và $K_{tong} = K_{tt} + K_q$."],
            "solution": "1. Động năng tịnh tiến: $K_{tt} = \\frac{1}{2}mv^2$.\\n2. Động năng quay: $K_q = \\frac{1}{2}I\\omega^2 = \\frac{1}{2}\\left(\\frac{1}{2}mR^2\\right)\\left(\\frac{v}{R}\\right)^2 = \\frac{1}{4}mv^2$.\\n3. Tổng động năng: $K_{tong} = K_{tt} + K_q = \\frac{3}{4}mv^2$.\\n4. Tỉ lệ: $\\frac{K_q}{K_{tong}} = \\frac{1/4}{3/4} = \\frac{1}{3} \\approx 33.33\\%$."
        },
        {
            "id": "ch15_ex4",
            "type": "easy",
            "q": "Tính chu kỳ dao động điều hòa bé của con lắc đơn có chiều dài dây treo $l = 1.0\\,\\text{m}$ tại nơi có gia tốc trọng trường $g = 9.81\\,\\text{m/s}^2$.",
            "unit": "s",
            "ans": 2.01,
            "tol": 0.05,
            "hints": ["Áp dụng công thức kinh điển: $T = 2\\pi\\sqrt{l/g}$."],
            "solution": "$T = 2\\pi\\sqrt{\\frac{1.0}{9.81}} = 2\\pi \\times 0.3193 \\approx 2.006\\,\\text{s} \\approx 2.01\\,\\text{s}$."
        },
        {
            "id": "ch15_ex5",
            "type": "mid",
            "q": "Một viên đạn chì có khối lượng $m = 20\\,\\text{g}$ bay với vận tốc $v = 300\\,\\text{m/s}$ cắm vào một tấm gỗ dày và dừng lại. Giả sử $60\\%$ động năng ban đầu của đạn biến thành nội năng làm nóng chính viên đạn. Cho biết nhiệt dung riêng của chì là $c_{pb} = 130\\,\\text{J/(kg}\\cdot\\text{K)}$. Tính độ tăng nhiệt độ $\\Delta T$ của viên đạn ($^\\circ\\text{C}$ hoặc $\\text{K}$).",
            "unit": "K",
            "ans": 207.69,
            "tol": 1.0,
            "hints": ["Động năng ban đầu $K = \\frac{1}{2}mv^2$. Nhiệt lượng đạn nhận là $Q = 0.6 K = m c_{pb} \\Delta T$."],
            "solution": "1. Động năng ban đầu của viên đạn: $K = \\frac{1}{2} \\times 0.02 \\times 300^2 = 900\\,\\text{J}$.\\n2. Nhiệt lượng truyền vào đạn: $Q = 0.6 \\times 900 = 540\\,\\text{J}$.\\n3. Mặt khác $Q = m c_{pb} \\Delta T \\Rightarrow \\Delta T = \\frac{Q}{m c_{pb}} = \\frac{540}{0.02 \\times 130} = \\frac{540}{2.6} \\approx 207.69\\,\\text{K}$."
        },
        {
            "id": "ch15_ex6",
            "type": "mid",
            "q": "Một xilanh chứa $n = 1.0\\,\\text{mol}$ khí Heli (khí hiếm đơn nguyên tử $i=3$) ở nhiệt độ ban đầu $T_1 = 300\\,\\text{K}$. Khí giãn nở đoạn nhiệt sinh công cơ học $W = 1247\\,\\text{J}$ đẩy pittông ra ngoài. Tính nhiệt độ cuối $T_2$ của khí (K). Cho $R = 8.314\\,\\text{J/(mol}\\cdot\\text{K)}$.",
            "unit": "K",
            "ans": 200.01,
            "tol": 1.0,
            "hints": ["Quá trình đoạn nhiệt: $Q = 0 \\Rightarrow \\Delta U = -W$. Với khí đơn nguyên tử, $\\Delta U = n C_v (T_2 - T_1) = n \\frac{3}{2}R (T_2 - T_1)$."],
            "solution": "1. Theo nguyên lý I: $Q = \\Delta U + W = 0 \\Rightarrow \\Delta U = -W = -1247\\,\\text{J}$.\\n2. Nội năng biến thiên: $\\Delta U = n \\frac{3}{2}R (T_2 - T_1) = 1.0 \\times 1.5 \\times 8.314 \\times (T_2 - 300) = 12.471 (T_2 - 300)$.\\n3. Ta có: $12.471(T_2 - 300) = -1247 \\Rightarrow T_2 - 300 = -1247 / 12.471 \\approx -99.99\\,\\text{K} \\Rightarrow T_2 \\approx 200.01\\,\\text{K}$."
        },
        {
            "id": "ch15_ex7",
            "type": "mid",
            "q": "Tính tốc độ truyền sóng âm trong không khí ở nhiệt độ $t = 20^\\circ\\text{C}$ ($T = 293.15\\,\\text{K}$). Cho biết khối lượng mol trung bình của không khí $M = 29\\,\\text{g/mol} = 0.029\\,\\text{kg/mol}$, hệ số đoạn nhiệt $\\gamma = 1.4$ và hằng số khí $R = 8.314\\,\\text{J/(mol}\\cdot\\text{K)}$.",
            "unit": "m/s",
            "ans": 343.02,
            "tol": 0.5,
            "hints": ["Áp dụng công thức Laplace cho vận tốc âm trong chất khí: $v = \\sqrt{\\frac{\\gamma R T}{M}}$."],
            "solution": "1. Thay số vào hệ thức Laplace:\\n   $v = \\sqrt{\\frac{1.4 \\times 8.314 \\times 293.15}{0.029}} = \\sqrt{\\frac{3412.15}{0.029}} = \\sqrt{117660.3} \\approx 343.02\\,\\text{m/s}$."
        },
        {
            "id": "ch15_ex8",
            "type": "mid",
            "q": "Một thanh mảnh đồng chất có chiều dài $L = 1.2\\,\\text{m}$ và khối lượng $M = 2.0\\,\\text{kg}$. Tính momen quán tính $I$ của thanh đối với trục quay vuông góc với thanh và đi qua điểm cách một đầu thanh một khoảng bằng $L/3$.",
            "unit": "kg.m^2",
            "ans": 0.32,
            "tol": 0.01,
            "hints": ["Khối tâm thanh ở chính giữa $L/2$. Khoảng cách từ trục đến khối tâm là $d = L/2 - L/3 = L/6$. Áp dụng định lý Steiner - Huygens: $I = I_{cm} + M d^2$, với $I_{cm} = \\frac{1}{12}ML^2$."],
            "solution": "1. Momen quán tính qua khối tâm: $I_{cm} = \\frac{1}{12} M L^2$.\\n2. Khoảng cách d: $d = \\frac{L}{2} - \\frac{L}{3} = \\frac{L}{6}$.\\n3. Theo định lý Steiner: $I = \\frac{1}{12} M L^2 + M \\left(\\frac{L}{6}\\right)^2 = M L^2 \\left(\\frac{1}{12} + \\frac{1}{36}\\right) = \\frac{4}{36} M L^2 = \\frac{1}{9} M L^2$.\\n4. Thay số: $I = \\frac{1}{9} \\times 2.0 \\times (1.2)^2 = \\frac{1}{9} \\times 2.0 \\times 1.44 = 0.32\\,\\text{kg}\\cdot\\text{m}^2$."
        },
        {
            "id": "ch15_ex9",
            "type": "hard",
            "q": "Một tàu vũ trụ khối lượng $m = 500\\,\\text{kg}$ đang chuyển động trên quỹ đạo tròn quanh Trái Đất có bán kính $r_1 = 2 R_d$. Động cơ kích hoạt để chuyển tàu lên quỹ đạo tròn cao hơn có bán kính $r_2 = 3 R_d$. Cho $M_d = 5.97 \\times 10^{24}\\,\\text{kg}$, $R_d = 6370\\,\\text{km}$, $G = 6.674 \\times 10^{-11}\\,\\text{N}\\cdot\\text{m}^2/\\text{kg}^2$. Tính độ biến thiên cơ năng $\\Delta E$ của tàu (theo đơn vị Gigajoule, $\\text{GJ}$).",
            "unit": "GJ",
            "ans": 2.61,
            "tol": 0.05,
            "hints": ["Cơ năng trên quỹ đạo tròn bán kính $r$ là $E = -\\frac{G M m}{2r}$. Độ biến thiên cơ năng là $\\Delta E = E(r_2) - E(r_1) = \\frac{G M m}{2}\\left(\\frac{1}{r_1} - \\frac{1}{r_2}\\right)$."],
            "solution": "1. Ta có: $\\Delta E = \\frac{G M_d m}{2} \\left(\\frac{1}{2R_d} - \\frac{1}{3R_d}\\right) = \\frac{G M_d m}{12 R_d}$.\\n2. Thay số:\\n   $G M_d = 6.674 \\times 10^{-11} \\times 5.97 \\times 10^{24} = 3.9844 \\times 10^{14}\\,\\text{m}^3/\\text{s}^2$.\\n   $\\Delta E = \\frac{3.9844 \\times 10^{14} \\times 500}{12 \\times 6.370 \\times 10^6} = \\frac{1.9922 \\times 10^{17}}{7.644 \\times 10^7} \\approx 2.6062 \\times 10^9\\,\\text{J} \\approx 2.61\\,\\text{GJ}$."
        },
        {
            "id": "ch15_ex10",
            "type": "hard",
            "q": "Một xilanh thẳng đứng tiết diện $S = 100\\,\\text{cm}^2 = 0.01\\,\\text{m}^2$ được đậy kín bởi một pittông nặng $M = 10\\,\\text{kg}$. Bên trong chứa $n = 0.1\\,\\text{mol}$ khí lý tưởng ở $T_1 = 300\\,\\text{K}$. Pittông được gắn với một lò xo thẳng đứng độ cứng $k = 500\\,\\text{N/m}$ (khi ở trạng thái ban đầu lò xo không biến dạng). Cho áp suất khí quyển $p_0 = 10^5\\,\\text{Pa}$, gia tốc $g = 9.8\\,\\text{m/s}^2$ và $R = 8.314\\,\\text{J/(mol}\\cdot\\text{K)}$. Khi đốt nóng khí từ từ đến nhiệt độ $T_2 = 450\\,\\text{K}$, pittông nâng lên một đoạn $x$. Tính $x$ theo đơn vị $\\text{cm}$.",
            "unit": "cm",
            "ans": 9.89,
            "tol": 0.2,
            "hints": ["Áp suất khí khi pittông dâng cao $x$ là $p(x) = p_0 + \\frac{Mg}{S} + \\frac{kx}{S} = p_1 + \\frac{kx}{S}$. Thể tích khí $V(x) = V_1 + Sx$. Phương trình khí: $p(x)V(x) = nRT_2$. Thiết lập phương trình bậc hai đối với $x$."],
            "solution": "1. Trạng thái 1:\\n   $p_1 = p_0 + \\frac{Mg}{S} = 100000 + \\frac{10 \\times 9.8}{0.01} = 109800\\,\\text{Pa}$.\\n   $V_1 = \\frac{nRT_1}{p_1} = \\frac{0.1 \\times 8.314 \\times 300}{109800} = \\frac{249.42}{109800} \\approx 2.27158 \\times 10^{-3}\\,\\text{m}^3$.\\n2. Trạng thái 2 khi dâng lên $x$:\\n   $p_2 = p_1 + \\frac{kx}{S}$, $V_2 = V_1 + Sx$.\\n   Phương trình trạng thái: $(p_1 + \\frac{kx}{S})(V_1 + Sx) = nRT_2 = 374.13\\,\\text{J}$.\\n   Khai triển: $p_1 V_1 + (p_1 S + \\frac{k V_1}{S})x + k x^2 = nRT_2$.\\n   Vì $p_1 V_1 = nRT_1 = 249.42$, phương trình trở thành:\\n   $k x^2 + (p_1 S + \\frac{k V_1}{S})x - nR(T_2 - T_1) = 0$.\\n3. Các hệ số bậc hai:\\n   $A = k = 500\\,\\text{N/m}$.\\n   $B = p_1 S + \\frac{k V_1}{S} = 109800 \\times 0.01 + \\frac{500 \\times 2.27158 \\times 10^{-3}}{0.01} = 1098 + 113.58 = 1211.58\\,\\text{N}$.\\n   $C = -nR\\Delta T = -(374.13 - 249.42) = -124.71\\,\\text{J}$.\\n4. Giải phương trình $500 x^2 + 1211.58 x - 124.71 = 0$:\\n   $\\Delta = 1211.58^2 - 4 \\times 500 \\times (-124.71) = 1467926 + 249420 = 1717346$.\\n   $\\sqrt{\\Delta} \\approx 1310.476$.\\n   $x = \\frac{-1211.58 + 1310.476}{1000} = \\frac{98.896}{1000} \\approx 0.0989\\,\\text{m} = 9.89\\,\\text{cm}$."
        }
    ]
}

CH16 = {
    "id": 16,
    "num": 16,
    "part": "Phần IV — Bảng tổng kết & Phương pháp",
    "title": "Phương pháp giải bài tập và Lỗi thường gặp",
    "tag": "Quy trình 5 bước & Bẫy đề thi kinh điển",
    "status": "ready",
    "summary": "Quy trình giải bài tập vật lý đại cương 5 bước chuẩn mực quốc tế, phân tích chi tiết các bẫy đề thi trắc nghiệm và tự luận phổ biến nhất, phương pháp kiểm tra nghiệm biên và thứ nguyên, cùng bộ bài tập bẫy cao rèn luyện phản xạ.",
    "nature": {
        "why": "Phần lớn sinh viên mất điểm trong các kỳ thi không phải vì không nhớ công thức, mà vì áp dụng sai điều kiện biên, nhầm chiều vectơ/dấu đại số, hoặc dùng công thức cơ bản cho các trường hợp không được phép áp dụng.",
        "meaning": "Tư duy vật lý chân chính đi từ: Quan sát mô hình thực tế -> Tách biệt hệ và môi trường -> Vẽ giản đồ tương tác lực (FBD) -> Thiết lập các định luật cơ bản ở dạng vi phân/bảo toàn -> Giải giải tích nghiệm chữ -> Thử lại thứ nguyên và cận biên trước khi thay số.",
        "conditions": "Quy trình áp dụng xuyên suốt cho tất cả các phân môn: Cơ học chất điểm, Vật rắn, Thủy động học, Dao động, Sóng và Nhiệt động lực học.",
        "limits": "Không có một công thức chung duy nhất cho mọi hiện tượng; điều cốt tử là phát hiện được bản chất đối xứng hoặc tương tác chiếm ưu thế trong từng bài toán cụ thể."
    },
    "formulas": [
        {
            "name": "Quy trình 5 bước kinh điển giải bài toán Vật lý",
            "latex": "\\text{Mô hình hóa} \\xrightarrow{(1)} \\text{Giản đồ FBD} \\xrightarrow{(2)} \\text{Phương trình vi phân / bảo toàn} \\xrightarrow{(3)} \\text{Nghiệm chữ} \\xrightarrow{(4)} \\text{Kiểm tra thứ nguyên & Biên} \\xrightarrow{(5)}",
            "meaning": "Quy trình chuẩn mực rèn luyện tư duy khoa học chính xác, loại bỏ hoàn toàn các lỗi sai logic và nhầm lẫn cơ bản.",
            "proof": [
                {"step": "\\text{Bước 1: Mô hình hóa}", "reason": "Xác định rõ đối tượng: chất điểm, hệ chất điểm, vật rắn, chất lưu lý tưởng hay khối khí"},
                {"step": "\\text{Bước 2: Giản đồ tương tác (FBD)}", "reason": "Liệt kê tất cả các lực tác dụng; nếu hệ quy chiếu phi quán tính thì bắt buộc bổ sung lực quán tính"},
                {"step": "\\text{Bước 3: Thiết lập phương trình cơ bản}", "reason": "Áp dụng định luật II Newton, định luật biến thiên động lượng/momen động lượng hoặc nguyên lý nhiệt động"},
                {"step": "\\text{Bước 4: Giải nghiệm giải tích}", "reason": "Biến đổi đại số tìm biểu thức nghiệm dưới dạng ký hiệu chữ trước khi thay số"},
                {"step": "\\text{Bước 5: Thử lại giới hạn biên & Thứ nguyên}", "reason": "Cho các tham số tiến tới 0 hoặc vô cùng để xem kết quả có phù hợp trực giác vật lý không"}
            ]
        },
        {
            "name": "Kiểm tra giới hạn biên (Limiting Case Analysis)",
            "latex": "a = \\frac{m_1 - m_2}{m_1 + m_2} g \\implies \\lim_{m_1 \\gg m_2} a = g; \\quad \\lim_{m_1 = m_2} a = 0",
            "meaning": "Thử nghiệm cực trị giúp phát hiện 90% lỗi biến đổi đại số hoặc nhầm dấu ngay trong phòng thi.",
            "proof": [
                {"step": "a = \\frac{1 - m_2/m_1}{1 + m_2/m_1} g", "reason": "Chia cả tử và mẫu cho m1"},
                {"step": "\\lim_{m_1 \\to \\infty} \\frac{m_2}{m_1} = 0 \\implies a = g", "reason": "Khi vật 1 quá nặng so với vật 2, vật 1 rơi tự do với gia tốc g"},
                {"step": "m_1 = m_2 \\implies a = 0", "reason": "Hai vật có khối lượng bằng nhau thì hệ cân bằng tĩnh hoặc chuyển động thẳng đều"}
            ]
        }
    ],
    "types": [
        {
            "name": "Bẫy 1: Quên lực quán tính trong hệ quy chiếu gia tốc (phi quán tính)",
            "algorithm": [
                "Bước 1: Xác định rõ hệ quy chiếu đang khảo sát: Hệ quy chiếu gắn với Trái Đất là hệ quán tính (xấp xỉ); hệ quy chiếu gắn với xe tăng tốc, thang máy, đĩa quay là phi quán tính.",
                "Bước 2: Trong hệ quy chiếu tịnh tiến có gia tốc $\\vec{a}_0$, bắt buộc thêm lực quán tính tịnh tiến: $\\vec{F}_{qt} = -m\\vec{a}_0$.",
                "Bước 3: Trong hệ quy chiếu quay với vận tốc góc $\\vec{\\omega}$, bắt buộc thêm lực ly tâm $\\vec{F}_{lt} = m\\omega^2\\vec{r}$ và lực Coriolis $\\vec{F}_{Cor} = 2m(\\vec{v}' \\times \\vec{\\omega})$.",
                "Bước 4: Viết phương trình cân bằng hoặc động lực học trong hệ phi quán tính: $\\sum \\vec{F} + \\vec{F}_{qt} = m\\vec{a}'$."
            ]
        },
        {
            "name": "Bẫy 2: Chiều và độ lớn của lực ma sát nghỉ trong chuyển động lăn không trượt",
            "algorithm": [
                "Bước 1: Ghi nhớ: Lực ma sát nghỉ $F_{msn}$ KHÔNG mặc định bằng $\\mu N$! Hệ thức $F = \\mu N$ chỉ đúng ở trạng thái trượt hoặc cận kề trượt.",
                "Bước 2: Trong chuyển động lăn không trượt thuần túy, $F_{msn}$ là một ẩn số độc lập.",
                "Bước 3: Viết 2 phương trình độc lập: Phương trình chuyển động tịnh tiến của khối tâm $F_{tt} - F_{msn} = m a_c$ và phương trình quay quanh khối tâm $F_{msn} R = I_c \\beta$.",
                "Bước 4: Ráp điều kiện lăn không trượt $a_c = \\beta R$ để giải đồng thời gia tốc $a_c$ và độ lớn lực ma sát nghỉ $F_{msn}$. Sau đó kiểm tra điều kiện $F_{msn} \\le \\mu_n N$."
            ]
        },
        {
            "name": "Bẫy 3: Phân chia chiều trao đổi nhiệt trên đường biến đổi tuyến tính đồ thị p-V",
            "algorithm": [
                "Bước 1: Trên một đoạn thẳng bất kỳ nối 2 trạng thái trên đồ thị $p-V$, chất khí KHÔNG PHẢI chỉ nhận nhiệt hoặc chỉ tỏa nhiệt trên toàn đoạn!",
                "Bước 2: Viết phương trình đoạn thẳng $p = p(V)$ và phương trình vi phân nhiệt lượng: $dQ = dU + dW = \\frac{i}{2}(pdV + Vdp) + pdV$.",
                "Bước 3: Thay $dp = p'(V)dV$ vào biểu thức $dQ$ để nhận được $dQ = f(V)dV$.",
                "Bước 4: Giải phương trình $f(V) = 0$ tìm thể tích chuyển tiếp $V^*$. Đoạn nào $f(V) > 0$ là nhận nhiệt, đoạn nào $f(V) < 0$ là nhả nhiệt. Nhiệt lượng nhận vào chỉ tính trên phần $f(V) > 0$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ: Tìm điểm trao đổi nhiệt triệt tiêu trên đường biến đổi tuyến tính",
            "problem": "Một khối khí lý tưởng đơn nguyên tử biến đổi theo phương trình đoạn thẳng $p = p_0 - \\alpha V$. Xác định thể tích $V^*$ tại đó khí bắt đầu chuyển từ quá trình thu nhiệt sang quá trình tỏa nhiệt.",
            "analysis": "Khí thu nhiệt khi $dQ > 0$ và tỏa nhiệt khi $dQ < 0$. Do đó điểm đảo chiều chính là nghiệm của $dQ = 0$.",
            "solution": "1. Biểu thức vi phân nhiệt lượng:\\n   $dQ = dU + dW = n C_v dT + p dV = \\frac{3}{2}(p dV + V dp) + p dV = \\frac{5}{2} p dV + \\frac{3}{2} V dp$.\\n2. Từ phương trình đường thẳng $p = p_0 - \\alpha V$, ta có $dp = -\\alpha dV$.\\n3. Thay vào biểu thức $dQ$:\\n   $dQ = \\left[\\frac{5}{2}(p_0 - \\alpha V) - \\frac{3}{2}\\alpha V\\right] dV = \\left[\\frac{5}{2}p_0 - 4\\alpha V\\right] dV$.\\n4. Khí nhận nhiệt khi $dQ > 0$ và tỏa nhiệt khi $dQ < 0$. Điểm đảo chiều là khi $dQ = 0$:\\n   $\\frac{5}{2}p_0 - 4\\alpha V^* = 0 \\implies V^* = \\frac{5 p_0}{8 \\alpha}$.\\n   Đây là bẫy kinh điển: Rất nhiều học sinh giả định sai rằng trên cả đoạn thẳng khí luôn thu nhiệt!"
        }
    ],
    "pitfalls": [
        {
            "error": "Nhầm công thức chu kỳ con lắc đơn và con lắc nón",
            "fix": "Con lắc đơn dao động phẳng: $T = 2\\pi\\sqrt{L/g}$. Con lắc nón quay tròn quanh trục đứng nghiêng góc $\\theta$: $T = 2\\pi\\sqrt{\\frac{L\\cos\\theta}{g}}$.",
            "tip": "Khi $\\theta \\to 0^\\circ$ (góc rất nhỏ), $\\cos\\theta \\to 1$, chu kỳ con lắc nón tiến về đúng chu kỳ con lắc đơn."
        },
        {
            "error": "Bảo toàn cơ năng cho va chạm mềm (như đạn ghim vào gỗ)",
            "fix": "Trong va chạm mềm chỉ có ĐỘNG LƯỢNG được bảo toàn, CƠ NĂNG BỊ BIẾN BIẾN THÀNH NHIỆT.",
            "tip": "Chỉ áp dụng bảo toàn cơ năng ở giai đoạn SAU va chạm (khi hệ con lắc đã dính liền và lắc lên cao)."
        },
        {
            "error": "Cho lực căng hai bên ròng rọc bằng nhau khi ròng rọc có khối lượng",
            "fix": "Khi ròng rọc có quán tính $I$, lực căng hai bên bắt buộc phải khác nhau ($T_1 \\neq T_2$) để tạo momen quay $(T_1 - T_2)R = I\\beta$.",
            "tip": "Chỉ khi đề bài ghi rõ 'ròng rọc không có khối lượng hoặc khối lượng không đáng kể' thì mới có $T_1 = T_2$."
        },
        {
            "error": "Áp dụng công thức Carnot cho chu trình nhiệt động bất kỳ",
            "fix": "Hiệu suất $\\eta = 1 - T_2/T_1$ CHỈ ĐÚNG DUY NHẤT cho chu trình Carnot (gồm 2 đẳng nhiệt và 2 đoạn nhiệt).",
            "tip": "Với các chu trình khác (như tam giác, hình chữ nhật, Otto), bắt buộc phải tính trực tiếp $\\eta = W_{net} / Q_{nhan}$."
        }
    ],
    "exercises": [
        {
            "id": "ch16_ex1",
            "type": "easy",
            "q": "Một quả cầu nhỏ treo vào đầu sợi dây nhẹ không dãn dài $L = 1.0\\,\\text{m}$. Quả cầu quay tròn đều trong mặt phẳng nằm ngang sao cho sợi dây quét thành một mặt nón nghiêng góc $\\theta = 30^\\circ$ so với phương thẳng đứng. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính chu kỳ quay $T$ của con lắc (s).",
            "unit": "s",
            "ans": 1.87,
            "tol": 0.05,
            "hints": ["Coi chừng bẫy: Đây là con lắc nón chứ không phải con lắc đơn dao động phẳng! Chu kỳ là $T = 2\\pi\\sqrt{\\frac{L\\cos\\theta}{g}}$."],
            "solution": "1. Lực tác dụng lên vật: Trọng lực $\\vec{P}$ và lực căng dây $\\vec{T}$.\\n2. Chiếu lên trục thẳng đứng cân bằng: $T\\cos\\theta = mg \\Rightarrow T = \\frac{mg}{\\cos\\theta}$.\\n3. Chiếu lên phương hướng tâm: $F_{ht} = T\\sin\\theta = m\\omega^2 r = m\\omega^2 (L\\sin\\theta) \\Rightarrow \\omega^2 = \\frac{g}{L\\cos\\theta}$.\\n4. Chu kỳ quay: $T = \\frac{2\\pi}{\\omega} = 2\\pi\\sqrt{\\frac{L\\cos\\theta}{g}} = 2\\pi\\sqrt{\\frac{1.0 \\times \\cos 30^\\circ}{9.8}} = 2\\pi\\sqrt{\\frac{0.8660}{9.8}} \\approx 2\\pi \\times 0.2973 \\approx 1.87\\,\\text{s}$."
        },
        {
            "id": "ch16_ex2",
            "type": "easy",
            "q": "Một khối trượt khối lượng $m = 2.0\\,\\text{kg}$ trượt từ đỉnh mặt phẳng nghiêng góc $\\alpha = 30^\\circ$ so với phương ngang, chiều dài mặt dốc $s = 5.0\\,\\text{m}$. Hệ số ma sát trượt giữa vật và mặt dốc là $\\mu = 0.2$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính độ lớn công của lực ma sát tác dụng lên vật trên suốt đoạn đường dốc ($|A_{ms}|$, đơn vị J).",
            "unit": "J",
            "ans": 16.97,
            "tol": 0.5,
            "hints": ["Coi chừng bẫy: Áp lực vuông góc với mặt dốc là $N = mg\\cos\\alpha$ chứ không phải $mg\\sin\\alpha$! Công ma sát: $|A_{ms}| = \\mu N s$."],
            "solution": "1. Phản lực pháp tuyến: $N = mg\\cos\\alpha = 2.0 \\times 9.8 \\times \\cos 30^\\circ = 19.6 \\times 0.8660 \\approx 16.974\\,\\text{N}$.\\n2. Độ lớn lực ma sát trượt: $F_{ms} = \\mu N = 0.2 \\times 16.974 \\approx 3.395\\,\\text{N}$.\\n3. Độ lớn công của lực ma sát: $|A_{ms}| = F_{ms} \\cdot s = 3.395 \\times 5.0 \\approx 16.97\\,\\text{J}$."
        },
        {
            "id": "ch16_ex3",
            "type": "easy",
            "q": "Một khối khí oxy $O_2$ (khí lưỡng nguyên tử $i=5$, khối lượng mol $M = 32\\,\\text{g/mol}$) có khối lượng $m = 16\\,\\text{g}$ được nung nóng đẳng áp khiến nhiệt độ tăng thêm một lượng $\\Delta T = 50\\,\\text{K}$. Cho $R = 8.314\\,\\text{J/(mol}\\cdot\\text{K)}$. Tính nhiệt lượng $Q$ mà khí đã nhận vào (J).",
            "unit": "J",
            "ans": 727.48,
            "tol": 2.0,
            "hints": ["Coi chừng bẫy: Quá trình đẳng áp thì nhiệt dung mol là $C_p = \\frac{i+2}{2}R$, đừng nhầm với nhiệt dung đẳng tích $C_v = \\frac{i}{2}R$."],
            "solution": "1. Số mol khí: $n = \\frac{m}{M} = \\frac{16}{32} = 0.5\\,\\text{mol}$.\\n2. Vì là quá trình đẳng áp của khí lưỡng nguyên tử: $C_p = \\frac{5+2}{2}R = 3.5 R = 3.5 \\times 8.314 = 29.099\\,\\text{J/(mol}\\cdot\\text{K)}$.\\n3. Nhiệt lượng nhận: $Q = n C_p \\Delta T = 0.5 \\times 29.099 \\times 50 = 727.475\\,\\text{J} \\approx 727.48\\,\\text{J}$."
        },
        {
            "id": "ch16_ex4",
            "type": "easy",
            "q": "Một con lắc lò xo treo thẳng đứng. Khi vật ở vị trí cân bằng tĩnh, lò xo bị dãn một đoạn $\\Delta l_0 = 4.0\\,\\text{cm} = 0.04\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính chu kỳ dao động điều hòa tự do $T$ của con lắc (s).",
            "unit": "s",
            "ans": 0.401,
            "tol": 0.01,
            "hints": ["Coi chừng bẫy: Ở VTCB, $mg = k\\Delta l_0 \\Rightarrow \\frac{m}{k} = \\frac{\\Delta l_0}{g}$. Chu kỳ $T = 2\\pi\\sqrt{\\frac{\\Delta l_0}{g}}$, không cần biết $m$ hay $k$."],
            "solution": "1. Tại vị trí cân bằng: $k\\Delta l_0 = mg \\Rightarrow \\frac{m}{k} = \\frac{\\Delta l_0}{g}$.\\n2. Chu kỳ dao động: $T = 2\\pi\\sqrt{\\frac{m}{k}} = 2\\pi\\sqrt{\\frac{\\Delta l_0}{g}} = 2\\pi\\sqrt{\\frac{0.04}{9.8}} = 2\\pi \\times 0.06389 \\approx 0.4014\\,\\text{s} \\approx 0.401\\,\\text{s}$."
        },
        {
            "id": "ch16_ex5",
            "type": "mid",
            "q": "Một viên đạn khối lượng $m = 10\\,\\text{g}$ bay theo phương ngang với tốc độ $v_0$ cắm vào một khúc gỗ khối lượng $M = 990\\,\\text{g}$ đang treo yên lặng trên dây dài $L = 1.5\\,\\text{m}$. Sau va chạm mềm, cả hệ đạn và gỗ cùng bay lên làm dây treo lệch góc cực đại $\\theta_{max} = 60^\\circ$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính tốc độ ban đầu $v_0$ của viên đạn (m/s).",
            "unit": "m/s",
            "ans": 383.41,
            "tol": 2.0,
            "hints": ["Bẫy kinh điển: Tuyệt đối KHÔNG bảo toàn cơ năng lúc va chạm! Dùng bảo toàn động lượng cho quá trình va chạm mềm để tìm vận tốc hệ $V$, sau đó mới bảo toàn cơ năng khi hệ gỗ + đạn đu lên góc cực đại."],
            "solution": "1. Bảo toàn cơ năng trong quá trình đu lên góc cực đại $\\theta = 60^\\circ$:\\n   Độ cao cực đại: $h = L(1 - \\cos 60^\\circ) = 1.5 \\times (1 - 0.5) = 0.75\\,\\text{m}$.\\n   Vận tốc của hệ ngay sau va chạm: $V = \\sqrt{2gh} = \\sqrt{2 \\times 9.8 \\times 0.75} = \\sqrt{14.7} \\approx 3.8341\\,\\text{m/s}$.\\n2. Bảo toàn động lượng trong va chạm mềm:\\n   $m v_0 = (m + M) V \\Rightarrow v_0 = \\frac{m + M}{m} V = \\frac{0.01 + 0.99}{0.01} V = 100 V$.\\n3. Thay số:\\n   $v_0 = 100 \\times 3.8341 \\approx 383.41\\,\\text{m/s}$."
        },
        {
            "id": "ch16_ex6",
            "type": "mid",
            "q": "Hai vật khối lượng $m_1 = 3.0\\,\\text{kg}$ và $m_2 = 2.0\\,\\text{kg}$ nối với nhau bằng dây nhẹ không dãn vắt qua một ròng rọc hình đĩa tròn đặc đồng chất có khối lượng $M = 2.0\\,\\text{kg}$. Dây không trượt trên ròng rọc. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính gia tốc chuyển động $a$ của hai vật (m/s$^2$).",
            "unit": "m/s^2",
            "ans": 1.63,
            "tol": 0.05,
            "hints": ["Bẫy kinh điển: Ròng rọc có khối lượng nên lực căng hai bên $T_1 \\neq T_2$! Momen quán tính đĩa đặc $I = \\frac{1}{2}MR^2$. Phương trình quay ròng rọc: $(T_1 - T_2)R = I\\beta = \\frac{1}{2}MR^2 (a/R)$."],
            "solution": "1. Phương trình cho $m_1$: $m_1 g - T_1 = m_1 a \\Rightarrow T_1 = m_1(g - a)$.\\n2. Phương trình cho $m_2$: $T_2 - m_2 g = m_2 a \\Rightarrow T_2 = m_2(g + a)$.\\n3. Phương trình quay ròng rọc: $(T_1 - T_2)R = I\\beta = \\left(\\frac{1}{2}MR^2\\right)\\frac{a}{R} \\Rightarrow T_1 - T_2 = \\frac{1}{2}M a$.\\n4. Trừ hai phương trình lực căng:\\n   $(m_1 - m_2)g - (m_1 + m_2)a = \\frac{1}{2}M a \\Rightarrow a = \\frac{(m_1 - m_2)g}{m_1 + m_2 + \\frac{1}{2}M}$.\\n5. Thay số: $a = \\frac{(3.0 - 2.0) \\times 9.8}{3.0 + 2.0 + 1.0} = \\frac{9.8}{6.0} \\approx 1.633\\,\\text{m/s}^2 \\approx 1.63\\,\\text{m/s}^2$."
        },
        {
            "id": "ch16_ex7",
            "type": "mid",
            "q": "Một mol khí lý tưởng đơn nguyên tử ($i=3$) thực hiện chu trình tam giác trên đồ thị $p-V$: Trạng thái 1 ($p_1 = 1.0\\,\\text{bar}, V_1 = 10\\,\\text{l}$) sang trạng thái 2 đẳng tích ($p_2 = 3.0\\,\\text{bar}, V_2 = 10\\,\\text{l}$), sau đó biến đổi theo đoạn thẳng sang trạng thái 3 ($p_3 = 1.0\\,\\text{bar}, V_3 = 30\\,\\text{l}$), rồi trở về trạng thái 1 đẳng áp ($1\\,\\text{bar} = 10^5\\,\\text{Pa}$, $1\\,\\text{l} = 10^{-3}\\,\\text{m}^3$). Tính hiệu suất $\\eta$ của chu trình theo đơn vị phần trăm (%).",
            "unit": "%",
            "ans": 26.67,
            "tol": 0.5,
            "hints": ["Bẫy siêu kinh điển: Không thể dùng công thức Carnot! Trên đoạn thẳng 2->3, khí chỉ thu nhiệt từ $V=10\\,\\text{l}$ đến $V=25\\,\\text{l}$ (tại điểm $dQ=0$), sau đó lại tỏa nhiệt từ $25\\,\\text{l}$ đến $30\\,\\text{l}$. Tổng nhiệt thu vào là $Q_{nhan} = Q_{12} + Q_{2\\to V^*}$."],
            "solution": "1. Công sinh ra trong 1 chu trình = Diện tích tam giác:\\n   $W = \\frac{1}{2}(p_2 - p_1)(V_3 - V_1) = \\frac{1}{2} \\times (2 \\times 10^5) \\times (20 \\times 10^{-3}) = 2000\\,\\text{J}$.\\n2. Nhiệt nhận trên đoạn 1->2 (đẳng tích):\\n   $Q_{12} = n C_v (T_2 - T_1) = \\frac{3}{2} V_1(p_2 - p_1) = 1.5 \\times 0.01 \\times 2 \\times 10^5 = 3000\\,\\text{J}$.\\n3. Nhiệt nhận trên đường thẳng 2->3:\\n   Phương trình đường 2-3: $p(V) = 3 \\times 10^5 - 10^7 (V - 0.01) = 4 \\times 10^5 - 10^7 V$.\\n   Vi phân nhiệt: $dQ = \\frac{5}{2}p dV + \\frac{3}{2}V dp = [10^6 - 4 \\times 10^7 V] dV$.\\n   $dQ > 0$ khi $V < 10^6 / (4 \\times 10^7) = 0.025\\,\\text{m}^3 = 25\\,\\text{l}$.\\n   Nhiệt thu từ $10\\,\\text{l}$ đến $25\\,\\text{l}$:\\n   $Q_{2\\to 25} = \\int_{0.01}^{0.025} (10^6 - 4 \\times 10^7 V) dV = [10^6 V - 2 \\times 10^7 V^2]_{0.01}^{0.025} = 4500\\,\\text{J}$.\\n4. Tổng nhiệt lượng nhận: $Q_{nhan} = 3000 + 4500 = 7500\\,\\text{J}$.\\n5. Hiệu suất: $\\eta = \\frac{W}{Q_{nhan}} = \\frac{2000}{7500} = \\frac{4}{15} \\approx 26.67\\%$."
        },
        {
            "id": "ch16_ex8",
            "type": "mid",
            "q": "Một vành tròn kim loại mỏng đồng chất bán kính $R = 0.3\\,\\text{m}$ được treo vào một điểm cố định trên mép vành và dao động với biên độ nhỏ quanh trục nằm ngang vuông góc với mặt phẳng vành. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính chu kỳ dao động nhỏ $T$ của vành tròn (s).",
            "unit": "s",
            "ans": 1.55,
            "tol": 0.05,
            "hints": ["Bẫy kinh điển: Vành tròn có $I_{cm} = mR^2$ (chứ không phải $\\frac{1}{2}mR^2$ như đĩa tròn). Theo định lý Steiner: $I = I_{cm} + md^2 = mR^2 + mR^2 = 2mR^2$ với $d=R$. Chu kỳ $T = 2\\pi\\sqrt{\\frac{I}{mgd}}$."],
            "solution": "1. Momen quán tính đối với trục treo ở mép:\\n   $I = I_{cm} + m R^2 = m R^2 + m R^2 = 2 m R^2$.\\n2. Chu kỳ dao động con lắc vật lý:\\n   $T = 2\\pi\\sqrt{\\frac{I}{m g d}} = 2\\pi\\sqrt{\\frac{2 m R^2}{m g R}} = 2\\pi\\sqrt{\\frac{2R}{g}}$.\\n3. Thay số:\\n   $T = 2\\pi\\sqrt{\\frac{2 \\times 0.3}{9.8}} = 2\\pi\\sqrt{\\frac{0.6}{9.8}} = 2\\pi \\times 0.2474 \\approx 1.554\\,\\text{s} \\approx 1.55\\,\\text{s}$."
        },
        {
            "id": "ch16_ex9",
            "type": "hard",
            "q": "Một quả cầu đặc đồng chất khối lượng $m = 2.0\\,\\text{kg}$, bán kính $R = 0.1\\,\\text{m}$ được đẩy trượt trên sàn ngang với vận tốc ban đầu $v_0 = 7.0\\,\\text{m/s}$ và không quay ($\\omega_0 = 0$). Hệ số ma sát trượt giữa quả cầu và sàn là $\\mu = 0.2$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính khoảng thời gian $t$ quả cầu trượt trên mặt sàn trước khi bắt đầu chuyển sang lăn không trượt thuần túy (s).",
            "unit": "s",
            "ans": 1.02,
            "tol": 0.05,
            "hints": ["Trong giai đoạn trượt: Lực ma sát $F_{ms} = \\mu mg$ làm giảm vận tốc tịnh tiến: $v(t) = v_0 - \\mu gt$, đồng thời sinh momen $M = F_{ms} R$ làm tăng tốc độ góc: $\\omega(t) = \\beta t$ với $\\beta = \\frac{M}{I} = \\frac{\\mu mg R}{\\frac{2}{5}mR^2}$. Điều kiện lăn không trượt là $v(t) = \\omega(t) R$."],
            "solution": "1. Gia tốc tịnh tiến: $a = -\\mu g \\Rightarrow v(t) = v_0 - \\mu gt$.\\n2. Gia tốc góc (momen quán tính quả cầu đặc $I = \\frac{2}{5}mR^2$):\\n   $\\beta = \\frac{F_{ms} R}{I} = \\frac{\\mu mg R}{\\frac{2}{5}mR^2} = \\frac{5 \\mu g}{2 R} \\Rightarrow \\omega(t) = \\frac{5 \\mu g}{2 R} t$.\\n3. Khi bắt đầu lăn không trượt thuần túy: $v(t) = \\omega(t) R$:\\n   $v_0 - \\mu gt = \\frac{5}{2} \\mu gt \\Rightarrow v_0 = \\frac{7}{2} \\mu gt \\Rightarrow t = \\frac{2 v_0}{7 \\mu g}$.\\n4. Thay số:\\n   $t = \\frac{2 \\times 7.0}{7 \\times 0.2 \\times 9.8} = \\frac{14.0}{13.72} \\approx 1.0204\\,\\text{s} \\approx 1.02\\,\\text{s}$."
        },
        {
            "id": "ch16_ex10",
            "type": "hard",
            "q": "Một sàn quay hình đĩa tròn đặc đồng chất có khối lượng $M = 100\\,\\text{kg}$, bán kính $R = 2.0\\,\\text{m}$ đang quay tự do quanh trục thẳng đứng không ma sát qua tâm với tốc độ góc $\\omega_0 = 1.0\\,\\text{rad/s}$. Một người có khối lượng $m = 60\\,\\text{kg}$ ban đầu đứng ở mép sàn, sau đó đi từ từ vào đúng tâm của sàn quay. Tính công cơ học $W$ do cơ bắp của người đó thực hiện trong quá trình di chuyển (J).",
            "unit": "J",
            "ans": 264.0,
            "tol": 5.0,
            "hints": ["Bẫy kinh điển: Cơ năng KHÔNG bảo toàn vì người đã dùng năng lượng cơ bắp để thắng lực quán tính ly tâm! Tuy nhiên, MOMEN ĐỘNG LƯỢNG của hệ (người + sàn) quanh trục quay là BẢO TOÀN tuyệt đối vì không có momen ngoại lực: $L_1 = L_2$. Từ đó tìm $\\omega_2$, công thực hiện bằng độ tăng động năng: $W = K_2 - K_1$."],
            "solution": "1. Momen quán tính của sàn quay: $I_{san} = \\frac{1}{2} M R^2 = \\frac{1}{2} \\times 100 \\times 2.0^2 = 200\\,\\text{kg}\\cdot\\text{m}^2$.\\n2. Trạng thái 1 (người ở mép sàn $r = R$):\\n   $I_1 = I_{san} + m R^2 = 200 + 60 \\times 2.0^2 = 200 + 240 = 440\\,\\text{kg}\\cdot\\text{m}^2$.\\n3. Trạng thái 2 (người ở tâm sàn $r = 0$):\\n   $I_2 = I_{san} + m \\times 0^2 = 200\\,\\text{kg}\\cdot\\text{m}^2$.\\n4. Áp dụng định luật bảo toàn momen động lượng:\\n   $I_1 \\omega_0 = I_2 \\omega_2 \\Rightarrow \\omega_2 = \\frac{I_1}{I_2} \\omega_0 = \\frac{440}{200} \\times 1.0 = 2.2\\,\\text{rad/s}$.\\n5. Động năng ban đầu và sau:\\n   $K_1 = \\frac{1}{2} I_1 \\omega_0^2 = \\frac{1}{2} \\times 440 \\times 1.0^2 = 220\\,\\text{J}$.\\n   $K_2 = \\frac{1}{2} I_2 \\omega_2^2 = \\frac{1}{2} \\times 200 \\times (2.2)^2 = 100 \\times 4.84 = 484\\,\\text{J}$.\\n6. Công của người thực hiện để thắng lực ly tâm đưa mình vào tâm:\\n   $W = K_2 - K_1 = 484 - 220 = 264.0\\,\\text{J}$."
        }
    ]
}

print("Chapter 15 and 16 data module ready.")
