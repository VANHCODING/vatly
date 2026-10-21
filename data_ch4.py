# -*- coding: utf-8 -*-
"""
Module defining chapter 4 data: Hệ chất điểm: Động lượng, Khối tâm, Va chạm
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

CH4 = {
    "id": 4,
    "num": 4,
    "part": "Phần I — Cơ học",
    "title": "Hệ chất điểm: Động lượng, Khối tâm, Va chạm",
    "tag": "Khối tâm & Định luật Bảo toàn",
    "status": "ready",
    "summary": "Nghiên cứu hệ chất điểm: Động lượng, định lý khối tâm, hệ quy chiếu khối tâm (hệ C), định lý König, các loại va chạm đàn hồi và mềm, chuyển động có khối lượng biến thiên (phương trình Tsiolkovsky).",
    "nature": {
        "why": "Mọi vật thể thực tế đều gồm vô số phân tử/nguyên tử tương tác phức tạp lẫn nhau. Định luật động lượng và khái niệm khối tâm cho phép quy chuyển động toàn cục của cả hệ về chuyển động của một chất điểm ảo tập trung toàn bộ khối lượng hệ mà không cần quan tâm đến các nội lực tương tác phức tạp bên trong.",
        "meaning": "Nội lực tuân theo định luật III Newton triệt tiêu từng cặp nên không thể làm thay đổi động lượng toàn phần của hệ. Khối tâm chuyển động như một chất điểm mang tổng khối lượng chịu tác dụng của tổng ngoại lực. Trong hệ quy chiếu khối tâm, tổng động lượng của hệ luôn luôn bằng 0, giúp việc phân tích va chạm và mất mát năng lượng trở nên sáng tỏ và đối xứng.",
        "conditions": "Định luật bảo toàn động lượng nghiệm đúng khi tổng ngoại lực tác dụng lên hệ bằng 0 (hệ cô lập) hoặc thời gian tương tác cực ngắn (va chạm, nổ) làm ngoại lực hoàn toàn không đáng kể so với nội lực.",
        "limits": "Khi có va chạm không đàn hồi (va chạm mềm), động lượng vẫn bảo toàn tuyệt đối nhưng cơ năng không bảo toàn do biến dạng dẻo và ma sát nội phân tử chuyển hóa thành nhiệt."
    },
    "formulas": [
        {
            "name": "Định lý biến thiên Động lượng và Xung lượng của lực",
            "latex": "\\vec{p} = m\\vec{v}; \\quad \\vec{J} = \\int_{t_1}^{t_2} \\vec{F} dt = \\Delta\\vec{p} = \\vec{p}_2 - \\vec{p}_1; \\quad \\frac{d\\vec{P}}{dt} = \\sum \\vec{F}^{ng}",
            "meaning": "Xung lượng của lực trong khoảng thời gian $\\Delta t$ đo mức độ truyền lượng chuyển động. Với hệ nhiều chất điểm, tổng nội lực triệt tiêu đôi một nên chỉ có ngoại lực mới làm biến đổi tổng động lượng $\\vec{P}$.",
            "proof": [
                {"step": "\\vec{F} = \\frac{d\\vec{p}}{dt} \\implies d\\vec{p} = \\vec{F} dt", "reason": "Dạng vi phân của định luật II Newton"},
                {"step": "\\vec{J} = \\int_{t_1}^{t_2} \\vec{F} dt = \\int_{\\vec{p}_1}^{\\vec{p}_2} d\\vec{p} = \\vec{p}_2 - \\vec{p}_1 = \\Delta\\vec{p}", "reason": "Lấy tích phân hai vế từ thời điểm t1 đến t2"},
                {"step": "\\vec{P} = \\sum_{i} \\vec{p}_i \\implies \\frac{d\\vec{P}}{dt} = \\sum_{i} \\frac{d\\vec{p}_i}{dt} = \\sum_{i} \\left( \\vec{F}_i^{ng} + \\sum_{j \\ne i} \\vec{F}_{ij} \\right)", "reason": "Tách lực tác dụng lên từng chất điểm thành ngoại lực và nội lực tương tác"},
                {"step": "\\sum_{i} \\sum_{j \\ne i} \\vec{F}_{ij} = \\vec{0}", "reason": "Theo định luật III Newton, các nội lực trực đối từng đôi một: F_ij = -F_ji"},
                {"step": "\\frac{d\\vec{P}}{dt} = \\sum_{i} \\vec{F}_i^{ng}", "reason": "Kết luận: Tốc độ biến thiên tổng động lượng bằng tổng các ngoại lực"}
            ]
        },
        {
            "name": "Định nghĩa và Chuyển động của Khối tâm",
            "latex": "\\vec{r}_{cm} = \\frac{\\sum m_i \\vec{r}_i}{M} = \\frac{1}{M}\\int \\vec{r}\\,dm; \\quad M\\vec{a}_{cm} = \\sum \\vec{F}^{ng}",
            "meaning": "Khối tâm chuyển động như một chất điểm có khối lượng $M = \\sum m_i$ chịu tác dụng của tổng ngoại lực. Ví dụ: Khi pháo hoa nổ giữa không trung, các mảnh pháo bay tứ phía nhưng khối tâm của chúng vẫn tiếp tục rơi theo quỹ đạo parabol.",
            "proof": [
                {"step": "M\\vec{r}_{cm} = \\sum m_i \\vec{r}_i", "reason": "Nhân tổng khối lượng M lên biểu thức định nghĩa khối tâm"},
                {"step": "M \\frac{d\\vec{r}_{cm}}{dt} = \\sum m_i \\frac{d\\vec{r}_i}{dt} \\implies M\\vec{v}_{cm} = \\sum m_i \\vec{v}_i = \\vec{P}", "reason": "Đạo hàm bậc nhất theo thời gian: Tổng động lượng hệ bằng M nhân vận tốc khối tâm"},
                {"step": "M \\frac{d\\vec{v}_{cm}}{dt} = \\frac{d\\vec{P}}{dt} = M\\vec{a}_{cm}", "reason": "Đạo hàm bậc hai theo thời gian"},
                {"step": "M\\vec{a}_{cm} = \\sum \\vec{F}^{ng}", "reason": "Thay biểu thức biến thiên động lượng của hệ vào phương trình gia tốc"}
            ],
            "svg": '<svg viewBox="0 0 380 160" class="svg-diagram"><defs><marker id="arrCm" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#6366f1"/></marker><marker id="arrVcm" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/></marker></defs><circle cx="60" cy="110" r="10" fill="#38bdf8"/><text x="55" y="114" fill="#fff" font-size="11">m1</text><circle cx="280" cy="50" r="14" fill="#f43f5e"/><text x="274" y="54" fill="#fff" font-size="11">m2</text><line x1="60" y1="110" x2="280" y2="50" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/><circle cx="215" cy="68" r="6" fill="#6366f1"/><text x="210" y="90" fill="#6366f1" font-weight="bold" font-size="13">G (Khối tâm)</text><line x1="215" y1="68" x2="275" y2="85" stroke="#10b981" stroke-width="3" marker-end="url(#arrVcm)"/><text x="280" y="95" fill="#10b981" font-weight="bold" font-size="13">v_cm</text><line x1="20" y1="150" x2="20" y2="20" stroke="#64748b" stroke-width="1.5"/><line x1="20" y1="150" x2="350" y2="150" stroke="#64748b" stroke-width="1.5"/><text x="355" y="153" fill="#64748b" font-size="12">x</text><text x="15" y="18" fill="#64748b" font-size="12">y</text></svg>'
        },
        {
            "name": "Hệ quy chiếu Khối tâm và Định lý König về Động năng",
            "latex": "K = \\frac{1}{2}M v_{cm}^2 + K'; \\quad K' = \\sum \\frac{1}{2}m_i v_i'^2 = \\frac{1}{2}\\mu v_{rel}^2 \\; (\\text{hệ 2 vật})",
            "meaning": "Động năng toàn phần của một hệ bằng động năng chuyển động tịnh tiến của khối tâm cộng với động năng chuyển động tương đối của các phần tử quanh khối tâm.",
            "proof": [
                {"step": "\\vec{v}_i = \\vec{v}_{cm} + \\vec{v}_i', \\quad \\text{với } \\sum m_i \\vec{v}_i' = \\vec{0}", "reason": "Phân tích vận tốc theo hệ quy chiếu khối tâm K' (tổng động lượng trong hệ K' luôn bằng 0)"},
                {"step": "K = \\sum \\frac{1}{2}m_i v_i^2 = \\sum \\frac{1}{2}m_i (\\vec{v}_{cm} + \\vec{v}_i')^2", "reason": "Thay biểu thức phân tích vận tốc vào định nghĩa động năng toàn phần"},
                {"step": "K = \\sum \\frac{1}{2}m_i v_{cm}^2 + \\vec{v}_{cm} \\cdot \\left(\\sum m_i \\vec{v}_i'\\right) + \\sum \\frac{1}{2}m_i v_i'^2", "reason": "Khai triển bình phương vô hướng của tổng hai vectơ"},
                {"step": "\\vec{v}_{cm} \\cdot \\left(\\sum m_i \\vec{v}_i'\\right) = \\vec{v}_{cm} \\cdot \\vec{0} = 0", "reason": "Số hạng chéo triệt tiêu hoàn toàn do tính chất cơ bản của hệ quy chiếu khối tâm"},
                {"step": "K = \\frac{1}{2}\\left(\\sum m_i\\right) v_{cm}^2 + \\sum \\frac{1}{2}m_i v_i'^2 = \\frac{1}{2}M v_{cm}^2 + K'", "reason": "Thu được công thức định lý König"}
            ]
        },
        {
            "name": "Va chạm đàn hồi xuyên tâm 1 chiều và Va chạm mềm",
            "latex": "v_1' = \\frac{(m_1 - m_2)v_1 + 2m_2 v_2}{m_1 + m_2}; \\quad v_2' = \\frac{(m_2 - m_1)v_2 + 2m_1 v_1}{m_1 + m_2}; \\quad \\vec{V}_{mem} = \\frac{m_1\\vec{v}_1 + m_2\\vec{v}_2}{m_1 + m_2}",
            "meaning": "Trong va chạm đàn hồi, cả động lượng và động năng đều bảo toàn ($e = 1$). Trong va chạm mềm, hai vật dính làm một và chuyển động với cùng vận tốc $V_{mem}$, động năng mất mát cực đại $\\Delta K = -\\frac{1}{2}\\mu v_{rel}^2$.",
            "proof": [
                {"step": "m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2' \\implies m_1(v_1 - v_1') = m_2(v_2' - v_2)", "reason": "Định luật bảo toàn động lượng"},
                {"step": "\\frac{1}{2}m_1 v_1^2 + \\frac{1}{2}m_2 v_2^2 = \\frac{1}{2}m_1 v_1'^2 + \\frac{1}{2}m_2 v_2'^2 \\implies m_1(v_1^2 - v_1'^2) = m_2(v_2'^2 - v_2^2)", "reason": "Định luật bảo toàn động năng trong va chạm đàn hồi"},
                {"step": "m_1(v_1 - v_1')(v_1 + v_1') = m_2(v_2' - v_2)(v_2' + v_2)", "reason": "Khai triển hiệu hai bình phương a² - b² = (a - b)(a + b)"},
                {"step": "v_1 + v_1' = v_2' + v_2 \\implies v_2' - v_1' = -(v_2 - v_1)", "reason": "Chia phương trình động năng cho phương trình động lượng (với v1 ≠ v1')"},
                {"step": "v_1' = \\frac{(m_1 - m_2)v_1 + 2m_2 v_2}{m_1 + m_2}", "reason": "Giải hệ phương trình bậc nhất hai ẩn v1' và v2'"}
            ]
        },
        {
            "name": "Phương trình chuyển động có khối lượng biến thiên (Tsiolkovsky)",
            "latex": "\\Delta v = u \\ln\\left(\\frac{m_0}{m}\\right); \\quad F_{day} = u \\left|\\frac{dm}{dt}\\right|",
            "meaning": "Tên lửa tăng tốc bằng phản lực do luồng khí phụt ra với vận tốc $u$ đối với tên lửa. Để tăng vận tốc theo cấp số cộng, khối lượng nhiên liệu ban đầu phải tăng theo cấp số nhân (hàm logarit tự nhiên).",
            "proof": [
                {"step": "m v = (m + dm)(v + dv) + (-dm)(v - u)", "reason": "Bảo toàn động lượng của hệ kín (tên lửa + khí phụt ra trong khoảng thời gian dt)"},
                {"step": "m v = m v + m dv + v dm + dm dv - v dm + u dm", "reason": "Khai triển các tích số"},
                {"step": "m dv + u dm = 0 \\implies dv = -u \\frac{dm}{m}", "reason": "Bỏ qua vi phân bậc hai dm·dv rất nhỏ và giản ước mv"},
                {"step": "\\int_{v_0}^v dv' = -u \\int_{m_0}^m \\frac{dm'}{m'} \\implies v - v_0 = -u \\ln\\left(\\frac{m}{m_0}\\right) = u \\ln\\left(\\frac{m_0}{m}\\right)", "reason": "Lấy tích phân xác định hai vế từ trạng thái ban đầu đến trạng thái cuối"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Xác định vị trí khối tâm của hệ chất điểm rời rạc và vật rắn liên tục",
            "algorithm": [
                "Bước 1: Chọn hệ trục tọa độ phù hợp (tận dụng tính đối xứng của vật để giảm số ẩn tọa độ).",
                "Bước 2: Với hệ rời rạc: Tính $x_{cm} = \\frac{\\sum m_i x_i}{M}$, $y_{cm} = \\frac{\\sum m_i y_i}{M}$.",
                "Bước 3: Với vật liên tục: Chia vật thành các phần tử vi phân $dm = \\lambda dl = \\sigma dS = \\rho dV$ rồi tính tích phân $x_{cm} = \\frac{1}{M}\\int x dm$.",
                "Bước 4: Kiểm tra kết quả: Khối tâm của vật đồng chất luôn nằm trên trục hoặc mặt phẳng đối xứng."
            ]
        },
        {
            "name": "Dạng 2: Bài toán va chạm đàn hồi và va chạm mềm",
            "algorithm": [
                "Bước 1: Chọn chiều dương trục tọa độ (thường chọn theo chiều chuyển động ban đầu của vật 1).",
                "Bước 2: Viết phương trình bảo toàn động lượng: $m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$ (chú ý dấu đại số của vận tốc).",
                "Bước 3: Nếu là va chạm đàn hồi: Viết thêm bảo toàn động năng hoặc hệ thức vận tốc tương đối $v_2' - v_1' = -(v_2 - v_1)$; Nếu là va chạm mềm: Vận tốc chung $V = \\frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$.",
                "Bước 4: Tính độ mất mát năng lượng $\\Delta K = K_{sau} - K_{truoc}$."
            ]
        },
        {
            "name": "Dạng 3: Chuyển động của hệ kín không có ngoại lực ngang (Người đi trên thuyền, vật trượt trên nêm)",
            "algorithm": [
                "Bước 1: Nhận diện ngoại lực: Nếu theo phương ngang $\\sum F_x^{ng} = 0$ thì động lượng theo phương ngang bảo toàn và khối tâm hệ không dịch chuyển theo phương ngang: $\\Delta x_{cm} = 0$.",
                "Bước 2: Biểu diễn độ dời của các vật qua độ dời tương đối và độ dời của hệ so với bờ.",
                "Bước 3: Thiết lập phương trình bảo toàn tọa độ khối tâm: $\\sum m_i \\Delta x_i = 0$.",
                "Bước 4: Giải phương trình tìm độ dịch chuyển của thuyền, bè hoặc nêm."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ 1: Con lắc thử đạn (Đo vận tốc viên đạn)",
            "problem": "Một viên đạn khối lượng $m = 10\\,\\text{g} = 0.01\\,\\text{kg}$ bay theo phương ngang với vận tốc $v_0$ cắm chặt vào một khối gỗ khối lượng $M = 1.99\\,\\text{kg}$ treo bởi dây nhẹ dài không dãn. Sau khi đạn cắm vào, khối gỗ chứa đạn nâng lên đến độ cao cực đại $h = 0.204\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính vận tốc ban đầu $v_0$ của viên đạn và phần trăm động năng đã bị thất thoát do va chạm.",
            "analysis": "Bài toán gồm hai giai đoạn rõ rệt:\\n- Giai đoạn 1 (Va chạm cực nhanh): Động lượng bảo toàn, cơ năng không bảo toàn (va chạm mềm).\\n- Giai đoạn 2 (Hệ dâng lên): Chỉ có trọng lực tác dụng, cơ năng bảo toàn.",
            "solution": "1. Giai đoạn 2: Khối gỗ chứa đạn dâng lên độ cao h:\\nBảo toàn cơ năng sau va chạm:\\n$$\\frac{1}{2}(m + M)V^2 = (m + M)gh \\implies V = \\sqrt{2gh}$$\\nThay số:\\n$$V = \\sqrt{2 \\times 9.8 \\times 0.204} = \\sqrt{3.9984} \\approx 2.0\\,\\text{m/s}$$\\n\\n2. Giai đoạn 1: Va chạm mềm giữa đạn và gỗ:\\nBảo toàn động lượng theo phương ngang:\\n$$m v_0 = (m + M)V \\implies v_0 = \\frac{m + M}{m}V$$\\nThay số:\\n$$v_0 = \\frac{0.01 + 1.99}{0.01} \\times 2.0 = \\frac{2.00}{0.01} \\times 2.0 = 200 \\times 2.0 = 400.0\\,\\text{m/s}$$\\n\\n3. Đánh giá phần trăm động năng thất thoát:\\n- Động năng ban đầu: $K_1 = \\frac{1}{2}m v_0^2 = \\frac{1}{2}(0.01)(400)^2 = 800\\,\\text{J}$\\n- Động năng ngay sau va chạm: $K_2 = \\frac{1}{2}(m + M)V^2 = \\frac{1}{2}(2.0)(2.0)^2 = 4\\,\\text{J}$\\n- Phần năng lượng mất đi biến thành nhiệt và biến dạng:\\n$$\\Delta K = K_1 - K_2 = 800 - 4 = 796\\,\\text{J}$$\\n$$\\%\\,\\text{thất thoát} = \\frac{796}{800} \\times 100\\% = 99.5\\%$$\\n(Nhận xét: Va chạm mềm làm thất thoát phần lớn động năng, khẳng định tuyệt đối không được dùng bảo toàn cơ năng trong lúc va chạm!)."
        },
        {
            "title": "Ví dụ 2: Người đi trên thuyền nổi tự do",
            "problem": "Một chiếc thuyền có khối lượng $M = 140\\,\\text{kg}$, chiều dài $L = 4\\,\\text{m}$ đang đứng yên trên mặt hồ yên ả. Một người có khối lượng $m = 60\\,\\text{kg}$ đứng ở đầu thuyền bắt đầu đi đều về phía đuôi thuyền. Bỏ qua mọi lực cản của nước. Hỏi khi người đó đến đuôi thuyền thì thuyền đã dịch chuyển được một đoạn bằng bao nhiêu mét so với bờ hồ?",
            "analysis": "Theo phương ngang, hệ (người + thuyền) không chịu ngoại lực nào tác dụng $\\implies$ Động lượng toàn phần theo phương ngang bảo toàn và bằng 0, vị trí khối tâm của hệ theo phương ngang đứng yên đối với bờ hồ.",
            "solution": "1. Chọn trục Ox nằm ngang gắn với bờ hồ, chiều dương là chiều người đi.\\nGọi $x$ là độ dịch chuyển của thuyền đối với bờ hồ (thuyền bị lùi ngược lại, mang dấu âm so với chiều người đi).\\n2. Độ dời của thuyền đối với bờ: $\\Delta x_T = -x$.\\nĐộ dời của người đối với thuyền là $+L$. Theo công thức cộng chuyển động, độ dời của người đối với bờ là:\\n$$\\Delta x_N = L - x$$\\n3. Do khối tâm hệ không đổi vị trí theo phương ngang ($M \\Delta x_T + m \\Delta x_N = 0$):\\n$$M(-x) + m(L - x) = 0 \\implies m L = (M + m)x$$\\n$$x = \\frac{m L}{M + m}$$\\n4. Thay các giá trị số:\\n$$x = \\frac{60 \\times 4}{140 + 60} = \\frac{240}{200} = 1.2\\,\\text{m}$$\\nĐáp số: Thuyền dịch chuyển lùi lại một đoạn 1.2 m so với bờ."
        }
    ],
    "pitfalls": [
        {
            "error": "Tự ý áp dụng định luật bảo toàn động năng trong va chạm mềm",
            "fix": "Chỉ có va chạm hoàn toàn đàn hồi mới bảo toàn động năng. Va chạm mềm (hai vật dính nhau) luôn làm tiêu hao động năng cực đại thành nhiệt năng.",
            "tip": "Động lượng luôn bảo toàn trong mọi loại va chạm kín (dù đàn hồi hay không đàn hồi), nhưng động năng thì chỉ bảo toàn khi đề bài ghi rõ 'va chạm đàn hồi'."
        },
        {
            "error": "Quên dấu vectơ (chiều dương) khi giải phương trình động lượng",
            "fix": "Động lượng là đại lượng vectơ $\\vec{p} = m\\vec{v}$. Khi hai vật chuyển động ngược chiều nhau, hình chiếu của vận tốc một vật phải mang dấu âm.",
            "tip": "Luôn vẽ một trục Ox và quy ước chiều dương rõ ràng trước khi viết phương trình đại số: $m_1 v_1 - m_2 v_2 = m_1 v_1' + m_2 v_2'$."
        },
        {
            "error": "Áp dụng công thức F = ma cho hệ có khối lượng biến thiên (như tên lửa, xích rơi)",
            "fix": "Định luật II nguyên bản của Newton là $\\vec{F} = \\frac{d\\vec{p}}{dt} = \\frac{d(m\\vec{v})}{dt}$. Khi khối lượng $m(t)$ thay đổi, $\\vec{F} \\ne m\\vec{a}$ mà phải dùng phương trình Meshchersky: $m\\frac{d\\vec{v}}{dt} = \\vec{F}^{ng} + \\vec{u}_{rel}\\frac{dm}{dt}$.",
            "tip": "Với tên lửa, lực đẩy do khối lượng phụt ra là $F_{day} = u |\\frac{dm}{dt}|$."
        }
    ],
    "exercises": [
        {
            "id": "ex_4_1",
            "type": "easy",
            "q": "Một hệ gồm hai chất điểm: $m_1 = 2\\,\\text{kg}$ chuyển động với vận tốc $v_1 = 4\\,\\text{m/s}$ theo chiều dương trục Ox, và chất điểm $m_2 = 3\\,\\text{kg}$ chuyển động với vận tốc $v_2 = 2\\,\\text{m/s}$ theo chiều âm trục Ox. Hãy tính tổng động lượng của hệ trên trục Ox.",
            "unit": "kg·m/s",
            "ans": 2.0,
            "tol": 0.05,
            "hints": [
                "Hình chiếu động lượng của chất điểm 1: $p_1 = m_1 v_1 = 2 \\times 4 = 8$.",
                "Hình chiếu động lượng của chất điểm 2 (ngược chiều): $p_2 = -m_2 v_2 = -3 \\times 2 = -6$.",
                "Tổng động lượng: $P_x = p_1 + p_2$."
            ],
            "solution": "Tổng động lượng của hệ hai chất điểm chiếu lên trục Ox:\\n$$P_x = m_1 v_1 - m_2 v_2 = (2)(4) - (3)(2) = 8 - 6 = 2.0\\,\\text{kg}\\cdot\\text{m/s}$$\\nĐáp số: 2.0 kg·m/s"
        },
        {
            "id": "ex_4_2",
            "type": "easy",
            "q": "Trên trục tọa độ Ox, chất điểm $m_1 = 1\\,\\text{kg}$ đặt tại tọa độ $x_1 = 2\\,\\text{m}$ và chất điểm $m_2 = 3\\,\\text{kg}$ đặt tại tọa độ $x_2 = 6\\,\\text{m}$. Hãy xác định tọa độ khối tâm $x_{cm}$ của hệ hai chất điểm này.",
            "unit": "m",
            "ans": 5.0,
            "tol": 0.05,
            "hints": [
                "Công thức tọa độ khối tâm hệ rời rạc: $x_{cm} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}$.",
                "Tổng khối lượng $M = 1 + 3 = 4\\,\\text{kg}$."
            ],
            "solution": "Áp dụng định nghĩa tọa độ khối tâm:\\n$$x_{cm} = \\frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = \\frac{(1)(2) + (3)(6)}{1 + 3} = \\frac{2 + 18}{4} = \\frac{20}{4} = 5.0\\,\\text{m}$$\\nĐáp số: 5.0 m"
        },
        {
            "id": "ex_4_3",
            "type": "easy",
            "q": "Một quả bóng khối lượng $m = 0.5\\,\\text{kg}$ bay với vận tốc $v = 12\\,\\text{m/s}$ đập vuông góc vào một bức tường phẳng rồi bật ngược trở lại theo phương cũ với cùng tốc độ $12\\,\\text{m/s}$. Hãy tính độ lớn xung lượng của lực do bức tường tác dụng lên quả bóng.",
            "unit": "N·s",
            "ans": 12.0,
            "tol": 0.05,
            "hints": [
                "Xung lượng của lực bằng độ biến thiên động lượng: $J = |\\Delta p| = |p_2 - p_1|$.",
                "Vì bóng đổi chiều chuyển động: $\\Delta p = m(-v) - mv = -2mv$."
            ],
            "solution": "Chọn chiều dương là chiều bay bật ngược trở lại của quả bóng:\\n$$p_1 = -m v, \\quad p_2 = +m v$$\\nĐộ biến thiên động lượng:\\n$$\\Delta p = p_2 - p_1 = m v - (-m v) = 2 m v$$\\nĐộ lớn xung lượng của lực:\\n$$J = 2 m v = 2 \\times 0.5 \\times 12 = 12.0\\,\\text{N}\\cdot\\text{s}$$\\nĐáp số: 12.0 N·s"
        },
        {
            "id": "ex_4_4",
            "type": "easy",
            "q": "Một toa xe lăn khối lượng $m_1 = 2\\,\\text{kg}$ chuyển động thẳng với vận tốc $v_1 = 6\\,\\text{m/s}$ đến va chạm mềm với một toa xe lăn khác có khối lượng $m_2 = 4\\,\\text{kg}$ đang đứng yên. Tính vận tốc của hai xe sau va chạm.",
            "unit": "m/s",
            "ans": 2.0,
            "tol": 0.05,
            "hints": [
                "Trong va chạm mềm, sau va chạm hai vật dính vào nhau và cùng chuyển động với vận tốc V.",
                "Bảo toàn động lượng: $m_1 v_1 = (m_1 + m_2)V \\implies V = \\frac{m_1 v_1}{m_1 + m_2}$."
            ],
            "solution": "Áp dụng định luật bảo toàn động lượng cho va chạm mềm:\\n$$m_1 v_1 + m_2 v_2 = (m_1 + m_2)V$$\\nVới $v_2 = 0$:\\n$$V = \\frac{m_1 v_1}{m_1 + m_2} = \\frac{2 \\times 6}{2 + 4} = \\frac{12}{6} = 2.0\\,\\text{m/s}$$\\nĐáp số: 2.0 m/s"
        },
        {
            "id": "ex_4_5",
            "type": "mid",
            "q": "Hai quả cầu va chạm đàn hồi trực diện 1 chiều: quả cầu 1 có $m_1 = 2\\,\\text{kg}$ chuyển động với vận tốc $v_1 = 5\\,\\text{m/s}$ đến va chạm với quả cầu 2 có $m_2 = 3\\,\\text{kg}$ đang chuyển động ngược chiều với vận tốc $v_2 = -2\\,\\text{m/s}$. Hãy tính vận tốc $v_1'$ của quả cầu 1 ngay sau va chạm.",
            "unit": "m/s",
            "ans": -3.4,
            "tol": 0.05,
            "hints": [
                "Áp dụng công thức giải tích cho va chạm đàn hồi xuyên tâm 1 chiều: $v_1' = \\frac{(m_1 - m_2)v_1 + 2m_2 v_2}{m_1 + m_2}$.",
                "Chú ý thay đúng dấu của $v_2 = -2\\,\\text{m/s}$."
            ],
            "solution": "Áp dụng công thức vận tốc sau va chạm đàn hồi 1 chiều:\\n$$v_1' = \\frac{(m_1 - m_2)v_1 + 2m_2 v_2}{m_1 + m_2}$$\\nThay các giá trị số:\\n$$v_1' = \\frac{(2 - 3)(5) + 2(3)(-2)}{2 + 3} = \\frac{-5 - 12}{5} = \\frac{-17}{5} = -3.4\\,\\text{m/s}$$\\n(Dấu âm nghĩa là quả cầu 1 bị bật dội ngược lại theo chiều âm với tốc độ 3.4 m/s).\\nĐáp số: -3.4 m/s"
        },
        {
            "id": "ex_4_6",
            "type": "mid",
            "q": "Trong thí nghiệm con lắc thử đạn, viên đạn có khối lượng $m = 10\\,\\text{g} = 0.01\\,\\text{kg}$ bay theo phương ngang cắm vào khối gỗ $M = 1.99\\,\\text{kg}$ treo trên dây. Sau va chạm, khối gỗ cùng đạn dâng lên đến độ cao $h = 0.204\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính vận tốc bay ban đầu $v_0$ của viên đạn.",
            "unit": "m/s",
            "ans": 400.0,
            "tol": 1.0,
            "hints": [
                "Vận tốc của hệ ngay sau va chạm: $V = \\sqrt{2gh} = \\sqrt{2 \\times 9.8 \\times 0.204} \\approx 2.0\\,\\text{m/s}$.",
                "Bảo toàn động lượng trước và sau va chạm: $m v_0 = (m + M)V \\implies v_0 = \\frac{m + M}{m}V$."
            ],
            "solution": "1. Vận tốc khối gỗ chứa đạn ngay sau va chạm:\\n$$V = \\sqrt{2gh} = \\sqrt{2 \\times 9.8 \\times 0.204} = \\sqrt{3.9984} \\approx 2.0\\,\\text{m/s}$$\\n2. Bảo toàn động lượng theo phương ngang khi đạn cắm vào gỗ:\\n$$m v_0 = (m + M)V \\implies v_0 = \\frac{m + M}{m}V$$\\nThay số:\\n$$v_0 = \\frac{0.01 + 1.99}{0.01} \\times 2.0 = \\frac{2.0}{0.01} \\times 2.0 = 200 \\times 2.0 = 400.0\\,\\text{m/s}$$\\nĐáp số: 400.0 m/s"
        },
        {
            "id": "ex_4_7",
            "type": "mid",
            "q": "Hai vật có khối lượng $m_1 = 3\\,\\text{kg}$ và $m_2 = 6\\,\\text{kg}$ chuyển động ngược chiều nhau với vận tốc lần lượt là $v_1 = 4\\,\\text{m/s}$ và $v_2 = -2\\,\\text{m/s}$. Hãy tính động năng chuyển động tương đối của hệ trong hệ quy chiếu khối tâm $K'$.",
            "unit": "J",
            "ans": 36.0,
            "tol": 0.1,
            "hints": [
                "Tính khối lượng rút gọn của hệ: $\\mu = \\frac{m_1 m_2}{m_1 + m_2}$.",
                "Vận tốc tương đối giữa hai vật: $v_{rel} = v_1 - v_2 = 4 - (-2) = 6\\,\\text{m/s}$.",
                "Động năng tương đối: $K' = \\frac{1}{2}\\mu v_{rel}^2$."
            ],
            "solution": "1. Khối lượng rút gọn của hệ hai vật:\\n$$\\mu = \\frac{m_1 m_2}{m_1 + m_2} = \\frac{3 \\times 6}{3 + 6} = \\frac{18}{9} = 2.0\\,\\text{kg}$$\\n2. Vận tốc tương đối giữa hai vật:\\n$$v_{rel} = v_1 - v_2 = 4 - (-2) = 6.0\\,\\text{m/s}$$\\n3. Động năng tương đối trong hệ quy chiếu khối tâm:\\n$$K' = \\frac{1}{2}\\mu v_{rel}^2 = \\frac{1}{2} \\times 2.0 \\times 6^2 = 36.0\\,\\text{J}$$\\nĐáp số: 36.0 J"
        },
        {
            "id": "ex_4_8",
            "type": "mid",
            "q": "Một chiếc thuyền chiều dài $L = 4\\,\\text{m}$, khối lượng $M = 140\\,\\text{kg}$ đang đứng yên trên mặt hồ không ma sát. Một người khối lượng $m = 60\\,\\text{kg}$ đi từ đầu mũi thuyền đến đuôi thuyền. Tính độ dịch chuyển của thuyền so với bờ hồ.",
            "unit": "m",
            "ans": 1.2,
            "tol": 0.05,
            "hints": [
                "Vì hệ không chịu ngoại lực ngang nên khối tâm của hệ người + thuyền đứng yên đối với bờ: $\\Delta x_{cm} = 0$.",
                "Công thức độ dịch chuyển của thuyền: $x = \\frac{m L}{M + m}$."
            ],
            "solution": "Do khối tâm của hệ người và thuyền không thay đổi vị trí theo phương ngang đối với bờ hồ:\\n$$M x = m(L - x) \\implies x = \\frac{m L}{M + m}$$\\nThay các giá trị số:\\n$$x = \\frac{60 \\times 4}{140 + 60} = \\frac{240}{200} = 1.2\\,\\text{m}$$\\nĐáp số: 1.2 m"
        },
        {
            "id": "ex_4_9",
            "type": "hard",
            "q": "Một tên lửa nghiên cứu vũ trụ có khối lượng ban đầu khi xuất phát là $m_0 = 10000\\,\\text{kg}$. Động cơ phản lực phụt khí với vận tốc không đổi $u = 2500\\,\\text{m/s}$ đối với tên lửa. Bỏ qua trọng lực và lực cản khí quyển. Để tên lửa đạt được độ tăng vận tốc $\\Delta v = 3500\\,\\text{m/s}$, khối lượng nhiên liệu đã bị tiêu thụ $\\Delta m = m_0 - m$ là bao nhiêu kilôgam?",
            "unit": "kg",
            "ans": 7534.0,
            "tol": 10.0,
            "hints": [
                "Áp dụng công thức Tsiolkovsky: $\\Delta v = u \\ln\\left(\\frac{m_0}{m}\\right)$.",
                "Rút ra tỉ số khối lượng: $\\frac{m_0}{m} = e^{\\Delta v / u}$.",
                "Tính khối lượng còn lại $m$ và suy ra lượng nhiên liệu đã đốt $\\Delta m = m_0 - m$."
            ],
            "solution": "Theo công thức Tsiolkovsky:\\n$$\\Delta v = u \\ln\\left(\\frac{m_0}{m}\\right) \\implies \\ln\\left(\\frac{m_0}{m}\\right) = \\frac{\\Delta v}{u} = \\frac{3500}{2500} = 1.4$$\\n$$\\frac{m_0}{m} = e^{1.4} \\approx 4.0552$$\\nKhối lượng còn lại của tên lửa sau khi tăng tốc:\\n$$m = \\frac{m_0}{4.0552} = \\frac{10000}{4.0552} \\approx 2465.97\\,\\text{kg}$$\\nKhối lượng nhiên liệu đã tiêu hao:\\n$$\\Delta m = m_0 - m = 10000 - 2465.97 \\approx 7534.0\\,\\text{kg}$$\\nĐáp số: 7534.0 kg"
        },
        {
            "id": "ex_4_10",
            "type": "hard",
            "q": "Thả một quả bóng từ độ cao $h_0 = 10\\,\\text{m}$ rơi xuống sàn nhà nằm ngang cứng. Hệ số phục hồi của mỗi lần va chạm giữa bóng và sàn là $e = 0.8$. Bỏ qua sức cản của không khí. Hãy tính tổng quãng đường mà quả bóng đi được kể từ lúc thả cho đến khi nảy hết và dừng hẳn trên sàn (làm tròn đến 2 chữ số thập phân).",
            "unit": "m",
            "ans": 45.56,
            "tol": 0.2,
            "hints": [
                "Sau va chạm thứ 1, bóng nảy lên độ cao $h_1 = e^2 h_0$.",
                "Sau đó bóng rơi xuống và nảy lên lần 2 đến độ cao $h_2 = e^4 h_0$...",
                "Tổng quãng đường là tổng cấp số nhân lùi vô hạn: $S = h_0 + 2(h_1 + h_2 + \\dots) = h_0 \\frac{1 + e^2}{1 - e^2}$."
            ],
            "solution": "Tổng quãng đường chuyển động của quả bóng gồm lần rơi đầu tiên $h_0$ và các lần nảy lên rồi rơi xuống $2h_k$:\\n$$S = h_0 + 2h_1 + 2h_2 + 2h_3 + \\dots$$\\nVới $h_k = e^{2k} h_0$, đây là một chuỗi cấp số nhân với công bội $q = e^2 < 1$:\\n$$S = h_0 + 2h_0 \\frac{e^2}{1 - e^2} = h_0 \\left(1 + \\frac{2e^2}{1 - e^2}\\right) = h_0 \\frac{1 + e^2}{1 - e^2}$$\\nThay $h_0 = 10\\,\\text{m}$ và $e = 0.8$ ($e^2 = 0.64$):\\n$$S = 10 \\times \\frac{1 + 0.64}{1 - 0.64} = 10 \\times \\frac{1.64}{0.36} = 10 \\times \\frac{41}{9} \\approx 45.5556 \\approx 45.56\\,\\text{m}$$\\nĐáp số: 45.56 m"
        }
    ]
}

print("Chapter 4 data module ready.")
