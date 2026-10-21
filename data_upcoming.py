# -*- coding: utf-8 -*-
"""
Module defining chapter skeletons for upcoming Chapters 6 to 16
Bám sát chính xác giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

UPCOMING_CHAPTERS = [
    {
        "id": 6,
        "num": 6,
        "part": "Phần I — Cơ học",
        "title": "Trường hấp dẫn",
        "tag": "Định lý Gauss & Các định luật Kepler",
        "status": "upcoming",
        "summary": "Định luật vạn vật hấp dẫn, cường độ trường hấp dẫn và điện thế hấp dẫn, định lý Gauss cho trường hấp dẫn, 3 định luật Kepler về chuyển động hành tinh, vận tốc vũ trụ cấp I và cấp II.",
        "nature": {
            "why": "Lực hấp dẫn là tương tác cơ bản chi phối quy mô vĩ mô của vũ trụ, giữ các hành tinh quay quanh Mặt Trời và các thiên hà liên kết với nhau.",
            "meaning": "Trường hấp dẫn là một trường thế xuyên tâm (lực hướng tâm bảo toàn momen động lượng). Định lý Gauss cho phép tính nhanh trường hấp dẫn của các vật thể đối xứng cầu. Các định luật Kepler là hệ quả chính xác của định luật nghịch đảo bình phương khoảng cách.",
            "conditions": "Áp dụng cho trường hấp dẫn yếu trong cơ học Newton (GM/(rc²) << 1).",
            "limits": "Trong trường hấp dẫn cực mạnh (gần lỗ đen, sao neutron) hoặc hiệu ứng dịch chuyển điểm cận nhật sao Thủy, phải dùng Thuyết tương đối rộng Einstein."
        },
        "formulas": [
            {"name": "Định luật vạn vật hấp dẫn", "latex": "\\vec{F} = -G\\frac{m_1 m_2}{r^2}\\vec{e}_r; \\quad G = 6.674 \\times 10^{-11}\\,\\text{N}\\cdot\\text{m}^2/\\text{kg}^2"},
            {"name": "Thế hấp dẫn và thế năng", "latex": "\\Phi(r) = -\\frac{GM}{r}; \\quad E_t(r) = -G\\frac{Mm}{r}"},
            {"name": "Định lý Kepler III", "latex": "\\frac{T^2}{a^3} = \\frac{4\\pi^2}{G(M + m)} \\approx \\frac{4\\pi^2}{GM}"},
            {"name": "Vận tốc vũ trụ cấp I và II", "latex": "v_I = \\sqrt{\\frac{GM}{R}} \\approx 7.9\\,\\text{km/s}; \\quad v_{II} = \\sqrt{\\frac{2GM}{R}} = \\sqrt{2}v_I \\approx 11.2\\,\\text{km/s}"}
        ]
    },
    {
        "id": 7,
        "num": 7,
        "part": "Phần I — Cơ học",
        "title": "Cơ học tương đối hẹp",
        "tag": "Biến đổi Lorentz & Động lực học tương đối tính",
        "status": "upcoming",
        "summary": "Hai tiên đề Einstein, phép biến đổi tọa độ Lorentz, hiện tượng co độ dài, giãn thời gian, nghịch lý cặp song sinh, công thức cộng vận tốc tương đối tính, khối lượng và hệ thức Einstein E = mc².",
        "nature": {
            "why": "Sự mâu thuẫn giữa phương trình Maxwell của điện từ học (tốc độ ánh sáng không đổi trong mọi hệ quán tính) và phép biến đổi Galilei cổ điển đòi hỏi phải tái định nghĩa cấu trúc không - thời gian.",
            "meaning": "Không gian và thời gian không còn tuyệt đối độc lập mà đan bện thành thể liên tục không - thời gian 4 chiều (Minkowski). Năng lượng và khối lượng tương đương qua hệ thức E = mc².",
            "conditions": "Áp dụng cho các hệ quy chiếu quán tính không có trường hấp dẫn lớn.",
            "limits": "Khi có gia tốc trường trọng lực mạnh, phải mở rộng sang Thuyết tương đối rộng."
        },
        "formulas": [
            {"name": "Phép biến đổi Lorentz", "latex": "x' = \\gamma(x - vt); \\quad t' = \\gamma\\left(t - \\frac{vx}{c^2}\\right); \\quad \\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}"},
            {"name": "Giãn thời gian và co độ dài", "latex": "\\Delta t = \\gamma \\Delta t_0; \\quad L = \\frac{L_0}{\\gamma}"},
            {"name": "Hệ thức năng lượng - xung lượng tương đối tính", "latex": "E = \\gamma m_0 c^2; \\quad E^2 = p^2 c^2 + m_0^2 c^4; \\quad E_d = (\\gamma - 1)m_0 c^2"}
        ]
    },
    {
        "id": 8,
        "num": 8,
        "part": "Phần I — Cơ học",
        "title": "Cơ học chất lưu",
        "tag": "Pascal, Bernoulli & Độ nhớt Poiseuille",
        "status": "upcoming",
        "summary": "Áp suất thủy tĩnh, nguyên lý Pascal, lực đẩy Archimedes, phương trình liên tục, phương trình Bernoulli cho chất lưu lý tưởng, chất lưu nhớt (định luật Poiseuille), hiện tượng bề mặt và mao dẫn.",
        "nature": {
            "why": "Chất lưu (chất lỏng và chất khí) không giữ hình dạng cố định mà có thể chảy dưới tác dụng của ứng suất tiếp, đòi hỏi phương pháp mô tả trường vận tốc và áp suất liên tục.",
            "meaning": "Phương trình Bernoulli là biểu hiện của định luật bảo toàn cơ năng trên một đường dòng chất lưu lý tưởng. Lực cản nội ma sát xuất hiện do sự trượt tương đối giữa các lớp chất lưu.",
            "conditions": "Phương trình Bernoulli chuẩn áp dụng cho chất lưu lý tưởng: Ổn định, không nén được (ρ = const), không nhớt (η = 0) và không xoáy.",
            "limits": "Khi chảy rối (Re > Re_th) hoặc chất lỏng có độ nhớt lớn, năng lượng cơ học hao tán thành nhiệt theo định luật Poiseuille."
        },
        "formulas": [
            {"name": "Phương trình thủy tĩnh", "latex": "p = p_0 + \\rho gh; \\quad dp = -\\rho g\\,dz"},
            {"name": "Phương trình liên tục", "latex": "S_1 v_1 = S_2 v_2 = Q_v = \\text{const}"},
            {"name": "Phương trình Bernoulli", "latex": "p + \\frac{1}{2}\\rho v^2 + \\rho gh = \\text{const}"},
            {"name": "Định luật Poiseuille cho ống tròn", "latex": "Q_v = \\frac{\\pi R^4 \\Delta p}{8\\eta L}"}
        ]
    },
    {
        "id": 9,
        "num": 9,
        "part": "Phần II — Dao động và Sóng cơ",
        "title": "Dao động cơ",
        "tag": "Điều hòa, Tắt dần & Cộng hưởng",
        "status": "upcoming",
        "summary": "Dao động điều hòa, con lắc lò xo, con lắc đơn, con lắc vật lý, năng lượng dao động, tổng hợp dao động cùng phương và vuông góc (hình Lissajous), dao động tắt dần, dao động cưỡng bức và hiện tượng cộng hưởng.",
        "nature": {
            "why": "Mọi hệ cân bằng bền bị kích thích nhẹ đều thực hiện dao động điều hòa quanh vị trí cân bằng do lực hồi phục tỷ lệ thuận với độ lệch.",
            "meaning": "Tần số riêng ω₀ chỉ phụ thuộc vào đặc tính cấu trúc của hệ (k và m). Khi có ngoại lực biến thiên tuần hoàn, biên độ dao động đạt cực đại tại tần số cộng hưởng ω ≈ ω₀.",
            "conditions": "Dao động điều hòa đòi hỏi góc lệch nhỏ (sin θ ≈ θ) và lực hồi phục tuân theo định luật Hooke.",
            "limits": "Khi biên độ lớn, xuất hiện tính phi tuyến (chu kỳ phụ thuộc biên độ). Khi ma sát quá lớn, hệ chuyển sang chế độ suy giảm phi dao động (quá cản)."
        },
        "formulas": [
            {"name": "Phương trình vi phân dao động điều hòa", "latex": "\\ddot{x} + \\omega_0^2 x = 0 \\implies x(t) = A\\cos(\\omega_0 t + \\varphi)"},
            {"name": "Con lắc vật lý và con lắc đơn", "latex": "\\omega_{vat\\,ly} = \\sqrt{\\frac{mgd}{I}}; \\quad \\omega_{don} = \\sqrt{\\frac{g}{\\ell}}"},
            {"name": "Dao động tắt dần", "latex": "\\ddot{x} + 2\\gamma\\dot{x} + \\omega_0^2 x = 0 \\implies x(t) = A_0 e^{-\\gamma t}\\cos(\\omega' t + \\varphi); \\; \\omega' = \\sqrt{\\omega_0^2 - \\gamma^2}"},
            {"name": "Biên độ dao động cưỡng bức", "latex": "A = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\Omega^2)^2 + 4\\gamma^2 \\Omega^2}}"}
        ]
    },
    {
        "id": 10,
        "num": 10,
        "part": "Phần II — Dao động và Sóng cơ",
        "title": "Sóng cơ",
        "tag": "Giao thoa, Sóng dừng & Doppler",
        "status": "upcoming",
        "summary": "Quá trình truyền pha dao động trong môi trường đàn hồi, phương trình sóng một chiều, vận tốc truyền sóng, năng lượng sóng và cường độ âm, giao thoa sóng, sóng dừng, hiệu ứng Doppler.",
        "nature": {
            "why": "Sóng là cơ chế lan truyền năng lượng và thông tin trong không gian mà không vận chuyển vật chất theo chiều truyền sóng.",
            "meaning": "Mỗi phần tử môi trường chỉ dao động tại chỗ quanh vị trí cân bằng. Sóng dừng hình thành do sự giao thoa của hai sóng kết hợp truyền ngược chiều nhau, tạo nên các nút đứng yên và bụng dao động cực đại.",
            "conditions": "Môi trường phải có tính đàn hồi và quán tính liên tục. Biên độ sóng đủ nhỏ để biến dạng nằm trong giới hạn đàn hồi tuyến tính.",
            "limits": "Sóng cơ không truyền được trong chân không. Trong môi trường phi tuyến, tốc độ sóng phụ thuộc biên độ (sóng xung kích shockwave)."
        },
        "formulas": [
            {"name": "Phương trình sóng phẳng một chiều", "latex": "u(x, t) = A\\cos\\left(\\omega t - \\frac{2\\pi x}{\\lambda} + \\varphi_0\\right) = A\\cos(\\omega t - kx + \\varphi_0)"},
            {"name": "Mối liên hệ giữa bước sóng, vận tốc và tần số", "latex": "\\lambda = v T = \\frac{v}{f}; \\quad v = \\sqrt{\\frac{B}{\\rho}} \\; (\\text{khí/lỏng}); \\; v = \\sqrt{\\frac{E}{\\rho}} \\; (\\text{rắn})"},
            {"name": "Cường độ âm và mức cường độ âm", "latex": "I = \\frac{1}{2}\\rho v \\omega^2 A^2; \\quad L = 10\\lg\\left(\\frac{I}{I_0}\\right)\\,(\\text{dB}); \\; I_0 = 10^{-12}\\,\\text{W/m}^2"},
            {"name": "Hiệu ứng Doppler cho sóng âm", "latex": "f' = f \\left(\\frac{v \\pm v_{thu}}{v \\mp v_{nguon}}\\right)"}
        ]
    },
    {
        "id": 11,
        "num": 11,
        "part": "Phần III — Nhiệt học",
        "title": "Khí lý tưởng và Thuyết động học phân tử",
        "tag": "Phân bố Maxwell - Boltzmann",
        "status": "upcoming",
        "summary": "Trạng thái nhiệt động, phương trình Clapeyron-Mendeleev, cơ sở thống kê của áp suất và nhiệt độ, định lý phân bố đều năng lượng theo bậc tự do, phân bố vận tốc Maxwell, phân bố độ cao Boltzmann, quãng đường tự do trung bình và các hiện tượng vận chuyển (khuếch tán, nội ma sát, dẫn nhiệt).",
        "nature": {
            "why": "Để hiểu các thông số vĩ mô (áp suất, nhiệt độ) từ bản chất chuyển động hỗn loạn nhiệt vi mô của hàng tỷ tỷ phân tử.",
            "meaning": "Áp suất là kết quả va chạm của vô số phân tử lên thành bình (p = 2/3 n ε_d). Nhiệt độ tuyệt đối là thước đo động năng tịnh tiến trung bình của phân tử (ε_d = 3/2 kT).",
            "conditions": "Khí lý tưởng: Thể tích riêng phân tử không đáng kể, không có lực tương tác từ xa trừ lúc va chạm đàn hồi.",
            "limits": "Ở nhiệt độ rất thấp hoặc áp suất rất cao, lực hút phân tử và thể tích riêng không còn bỏ qua được, phải dùng mô hình Khí thực Van der Waals."
        },
        "formulas": [
            {"name": "Phương trình trạng thái khí lý tưởng", "latex": "p V = n R T = N k T; \\quad p = \\frac{\\rho R T}{M}"},
            {"name": "Phương trình cơ bản thuyết động học", "latex": "p = \\frac{1}{3} n_0 m_0 \\overline{v^2} = \\frac{2}{3} n_0 \\overline{\\varepsilon}_d; \\quad \\overline{\\varepsilon}_d = \\frac{3}{2} k T"},
            {"name": "Các vận tốc đặc trưng Maxwell", "latex": "v_{xs} = \\sqrt{\\frac{2RT}{M}}; \\quad \\overline{v} = \\sqrt{\\frac{8RT}{\\pi M}}; \\quad v_{cb} = \\sqrt{\\frac{3RT}{M}}"},
            {"name": "Quãng đường tự do trung bình", "latex": "\\bar{\\lambda} = \\frac{1}{\\sqrt{2}\\pi d^2 n_0} = \\frac{kT}{\\sqrt{2}\\pi d^2 p}"}
        ]
    },
    {
        "id": 12,
        "num": 12,
        "part": "Phần III — Nhiệt học",
        "title": "Nguyên lý thứ nhất của Nhiệt động lực học",
        "tag": "Công, Nhiệt, Nội năng & Đa phương",
        "status": "upcoming",
        "summary": "Nội năng của khí lý tưởng, công vi phân trong biến đổi thể tích, nhiệt dung mol đẳng tích & đẳng áp (hệ thức Mayer), các quá trình cân bằng cơ bản (đẳng tích, đẳng áp, đẳng nhiệt, đoạn nhiệt) và quá trình đa phương tổng quát.",
        "nature": {
            "why": "Là sự mở rộng của Định luật bảo toàn và chuyển hóa năng lượng tổng quát cho các quá trình có trao đổi nhiệt năng.",
            "meaning": "Nội năng U là hàm trạng thái. Công A và nhiệt Q là hàm quá trình (phụ thuộc đường đi biến đổi).",
            "conditions": "Hệ nhiệt động kín thực hiện các quá trình biến đổi chuẩn tĩnh (cân bằng qua từng bước vi mô).",
            "limits": "Nguyên lý I chỉ cho biết năng lượng được bảo toàn nhưng không cho biết chiều tự phát của quá trình (cần đến Nguyên lý II)."
        },
        "formulas": [
            {"name": "Nguyên lý thứ nhất", "latex": "Q = \\Delta U + W; \\quad dU = \\delta Q - \\delta W = \\delta Q - p\\,dV"},
            {"name": "Nội năng và nhiệt dung mol", "latex": "U = \\frac{i}{2}n R T; \\quad C_v = \\frac{i}{2}R; \\quad C_p = C_v + R = \\frac{i+2}{2}R; \\quad \\gamma = \\frac{C_p}{C_v}"},
            {"name": "Phương trình đoạn nhiệt Poisson", "latex": "p V^\\gamma = \\text{const}; \\quad T V^{\\gamma - 1} = \\text{const}; \\quad T^\\gamma p^{1-\\gamma} = \\text{const}"},
            {"name": "Phương trình đa phương tổng quát", "latex": "p V^m = \\text{const}; \\quad C_m = C_v \\frac{m - \\gamma}{m - 1}; \\quad W = \\frac{p_1 V_1 - p_2 V_2}{m - 1}"}
        ]
    },
    {
        "id": 13,
        "num": 13,
        "part": "Phần III — Nhiệt học",
        "title": "Nguyên lý thứ hai và Entropy",
        "tag": "Chu trình Carnot, Clausius & Chiều hướng tự nhiên",
        "status": "upcoming",
        "summary": "Quá trình thuận nghịch và bất thuận nghịch, phát biểu Clausius và Kelvin-Planck, chu trình Carnot và định lý Carnot, bất đẳng thức Clausius, hàm trạng thái Entropy S, ý nghĩa thống kê của Entropy (công thức Boltzmann S = k ln Ω), chu trình động cơ thực tế.",
        "nature": {
            "why": "Xác định chiều diễn biến tự nhiên không thể đảo ngược của các quá trình vĩ mô: Nhiệt không thể tự động truyền từ vật lạnh sang vật nóng mà không có tác động từ ngoài.",
            "meaning": "Entropy là thước đo mức độ hỗn loạn vi mô của hệ cô lập. Tự nhiên luôn tự phát chuyển biến về trạng thái có xác suất nhiệt động lớn nhất (Entropy cực đại).",
            "conditions": "Hệ cô lập tự do diễn biến; định lý Carnot áp dụng cho động cơ nhiệt nhận nhiệt từ nguồn nóng T1 và nhả nhiệt cho nguồn lạnh T2.",
            "limits": "Không thể chế tạo động cơ nhiệt có hiệu suất 100% (bác bỏ động cơ vĩnh cửu loại II)."
        },
        "formulas": [
            {"name": "Hiệu suất chu trình Carnot lý tưởng", "latex": "\\eta_{Carnot} = 1 - \\frac{T_2}{T_1} = \\frac{Q_1 - |Q_2|}{Q_1}; \\quad \\frac{Q_1}{T_1} = \\frac{Q_2}{T_2}"},
            {"name": "Định nghĩa vi phân của Entropy", "latex": "dS = \\frac{\\delta Q_{rev}}{T}; \\quad \\Delta S = \\int_1^2 \\frac{\\delta Q_{rev}}{T}"},
            {"name": "Bất đẳng thức Clausius và nguyên lý tăng Entropy", "latex": "\\oint \\frac{\\delta Q}{T} \\le 0; \\quad \\Delta S_{he\\,co\\,lap} \\ge 0"},
            {"name": "Công thức thống kê Boltzmann", "latex": "S = k \\ln \\Omega"}
        ]
    },
    {
        "id": 14,
        "num": 14,
        "part": "Phần III — Nhiệt học",
        "title": "Khí thực và Chuyển pha",
        "tag": "Phương trình Van der Waals & Chuyển pha loại 1",
        "status": "upcoming",
        "summary": "Khí thực, lực tương tác phân tử Van der Waals, phương trình trạng thái Van der Waals, đường đẳng nhiệt thực nghiệm Andrews, trạng thái tới hạn (Tc, pc, Vc), chuyển pha loại 1 và phương trình Clapeyron-Clausius.",
        "nature": {
            "why": "Mô hình khí lý tưởng không giải thích được hiện tượng ngưng tụ khí thành lỏng và hành vi của chất khí ở áp suất cao.",
            "meaning": "Phương trình Van der Waals đưa vào hai số hiệu chỉnh: số hiệu chỉnh áp suất nội tại a/V_m² do lực hút phân tử và số hiệu chỉnh thể tích riêng b do kích thước chiếm chỗ của phân tử.",
            "conditions": "Áp dụng cho khí thực ở áp suất vừa và nhiệt độ không quá xa điểm ngưng tụ.",
            "limits": "Khi khí chuyển sang trạng thái siêu tới hạn (T > Tc), ranh giới giữa lỏng và khí biến mất hoàn toàn."
        },
        "formulas": [
            {"name": "Phương trình trạng thái Van der Waals (1 mol)", "latex": "\\left(p + \\frac{a}{V_m^2}\\right)(V_m - b) = R T"},
            {"name": "Các thông số tại điểm tới hạn", "latex": "V_{mc} = 3b; \\quad p_c = \\frac{a}{27b^2}; \\quad T_c = \\frac{8a}{27Rb}"},
            {"name": "Phương trình Clapeyron - Clausius", "latex": "\\frac{dp}{dT} = \\frac{L}{T(V_2 - V_1)}"}
        ]
    },
    {
        "id": 15,
        "num": 15,
        "part": "Phần IV — Bảng tổng kết & Phương pháp",
        "title": "Bảng công thức tổng hợp toàn diện",
        "tag": "Tra cứu nhanh & In ấn",
        "status": "upcoming",
        "summary": "Bảng tra cứu và in ấn toàn bộ các công thức cốt lõi của 14 chương Vật lý đại cương 1: Cơ học, Dao động & Sóng, Nhiệt học và các hằng số vật lý tiêu chuẩn SI.",
        "nature": {
            "why": "Giúp sinh viên hệ thống hóa kiến thức toàn diện trước kỳ thi và tra cứu nhanh các mối liên hệ chéo giữa các phần.",
            "meaning": "Cung cấp cái nhìn tổng quan xuyên suốt từ phương trình vi phân chuyển động đến các định luật bảo toàn vĩ mô.",
            "conditions": "Tra cứu kèm điều kiện áp dụng của từng công thức.",
            "limits": "Thuộc công thức không thay thế được việc hiểu bản chất vật lý."
        },
        "formulas": [
            {"name": "Bảng hằng số vật lý chuẩn", "latex": "g = 9.81\\,\\text{m/s}^2; \\; G = 6.674 \\times 10^{-11}; \\; c = 3.0 \\times 10^8; \\; R = 8.314; \\; N_A = 6.022 \\times 10^{23}; \\; k = 1.38 \\times 10^{-23}"}
        ]
    },
    {
        "id": 16,
        "num": 16,
        "part": "Phần IV — Bảng tổng kết & Phương pháp",
        "title": "Phương pháp giải bài tập và Lỗi thường gặp",
        "tag": "Chiến lược làm bài thi",
        "status": "upcoming",
        "summary": "Quy trình chuẩn 4 bước giải mọi bài toán vật lý đại cương, phân tích các bẫy đề thi trắc nghiệm và tự luận thường gặp, mẹo kiểm tra đáp số bằng thứ nguyên và giới hạn biên.",
        "nature": {
            "why": "Phần lớn sinh viên mất điểm không phải do không thuộc công thức mà do chọn sai hệ quy chiếu, thiếu lực liên kết, nhầm dấu đại số hoặc không kiểm tra giới hạn vật lý.",
            "meaning": "Rèn luyện tư duy khoa học: Đọc đề -> Vẽ hình mô hình hóa -> Viết phương trình bảo toàn / định luật -> Giải giải tích -> Thử lại thứ nguyên và cận biên.",
            "conditions": "Áp dụng xuyên suốt cho toàn bộ các đề thi học phần Vật lý đại cương 1.",
            "limits": "Cần luyện tập giải đề thường xuyên để nâng cao tốc độ bấm máy và phản xạ tư duy."
        },
        "formulas": [
            {"name": "Quy trình giải bài chuẩn mực", "latex": "\\text{Mô hình hóa} \\longrightarrow \\text{Phương trình vật lý} \\longrightarrow \\text{Nghiệm giải tích} \\longrightarrow \\text{Kiểm tra thứ nguyên}"}
        ]
    }
]

print("Upcoming chapters (6 to 16) data module ready.")
