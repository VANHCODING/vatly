# -*- coding: utf-8 -*-
"""
Module defining chapter 5 data: Động lực học vật rắn
Bám sát giáo trình Lương Duyên Bình và tài liệu Vat_ly_dai_cuong_1.pdf
"""

CH5 = {
    "id": 5,
    "num": 5,
    "part": "Phần I — Cơ học",
    "title": "Động lực học vật rắn",
    "tag": "Momen Quán tính & Lăn không trượt",
    "status": "ready",
    "summary": "Nghiên cứu chuyển động của vật rắn: Momen lực, momen động lượng, phương trình quay quanh trục cố định, momen quán tính và định lý Steiner, chuyển động song phẳng, lăn không trượt, bảo toàn momen động lượng và hiện tượng tiến động.",
    "nature": {
        "why": "Vật rắn là mô hình vật lý lý tưởng hóa khi khoảng cách giữa hai điểm bất kỳ luôn không đổi (liên kết cứng tuyệt đối). Khi vật quay, các điểm trên vật có cùng vận tốc góc $\\omega$ nhưng vận tốc dài $v = \\omega r$ khác nhau, nên không thể xem vật như một chất điểm mà phải tính đến sự phân bố khối lượng quanh trục quay thông qua đại lượng Momen quán tính $I$.",
        "meaning": "Momen lực $\\vec{M} = \\vec{r} \\times \\vec{F}$ đặc trưng cho tác dụng làm quay của lực (phụ thuộc vào cánh tay đòn $d$). Momen quán tính $I = \\int r^2 dm$ là số đo quán tính quay, đóng vai trò như khối lượng $m$ trong chuyển động tịnh tiến: Cùng một khối lượng nhưng vật nào có khối lượng phân bố càng xa trục quay thì $I$ càng lớn và càng khó làm quay. Chuyển động lăn không trượt là sự phối hợp mật thiết giữa chuyển động tịnh tiến của khối tâm và quay quanh khối tâm, trong đó lực ma sát nghỉ là lực liên kết giúp vật lăn mà không làm tiêu hao cơ năng.",
        "conditions": "Mô hình vật rắn giả thiết vật hoàn toàn không bị biến dạng khi chịu lực. Phương trình $M_z = I\\beta$ chỉ áp dụng cho trục quay cố định hoặc trục quay đi qua khối tâm và giữ nguyên phương trong không gian.",
        "limits": "Khi vật quay với tốc độ cực lớn, lực quán tính ly tâm có thể gây biến dạng dẻo hoặc phá hủy liên kết vật liệu. Trong chuyển động quay tự do 3 chiều không có trục cố định, vectơ momen động lượng $\\vec{L}$ nói chung không cùng phương với vectơ vận tốc góc $\\vec{\\omega}$, khi đó phải dùng công cụ Tensor quán tính đối xứng $3 \\times 3$."
    },
    "formulas": [
        {
            "name": "Momen lực và Phương trình cơ bản của Chuyển động quay",
            "latex": "\\vec{M} = \\vec{r} \\times \\vec{F}; \\quad M_z = I\\beta = I\\frac{d\\omega}{dt} = \\frac{dL_z}{dt}; \\quad L_z = I\\omega",
            "meaning": "Momen lực đối với một trục bằng tích momen quán tính với gia tốc góc. Tương tự như định luật II Newton cho chuyển động tịnh tiến ($F = ma$).",
            "proof": [
                {"step": "\\vec{L} = \\sum \\vec{r}_i \\times \\vec{p}_i = \\sum m_i (\\vec{r}_i \\times \\vec{v}_i)", "reason": "Định nghĩa vectơ momen động lượng của hệ chất điểm hợp thành vật rắn"},
                {"step": "v_i = \\omega r_i \\implies L_z = \\sum m_i r_i v_i = \\sum m_i r_i^2 \\omega = \\left(\\sum m_i r_i^2\\right)\\omega", "reason": "Chiếu lên trục quay z với các chất điểm quay tròn bán kính ri"},
                {"step": "I = \\sum m_i r_i^2 = \\int r^2 dm", "reason": "Định nghĩa momen quán tính I đối với trục quay z"},
                {"step": "L_z = I\\omega", "reason": "Mối liên hệ tuyến tính giữa momen động lượng và vận tốc góc"},
                {"step": "\\frac{dL_z}{dt} = \\frac{d(I\\omega)}{dt} = I\\frac{d\\omega}{dt} = I\\beta = M_z", "reason": "Đạo hàm theo thời gian (khi trục quay và phân bố khối lượng cố định thì I = const)"}
            ]
        },
        {
            "name": "Định lý trục song song Huygens - Steiner",
            "latex": "I_\\Delta = I_{cm} + m d^2",
            "meaning": "Momen quán tính của vật đối với một trục quay $\\Delta$ bất kỳ bằng momen quán tính đối với trục song song đi qua khối tâm cộng với tích khối lượng với bình phương khoảng cách giữa hai trục.",
            "proof": [
                {"step": "I_\\Delta = \\int r_i^2 dm = \\int (x_i^2 + y_i^2) dm", "reason": "Định nghĩa momen quán tính trong hệ tọa độ có trục z trùng trục Δ"},
                {"step": "x_i = x_i' + a, \\quad y_i = y_i' + b, \\quad \\text{với } d^2 = a^2 + b^2", "reason": "Phép tịnh tiến hệ trục tọa độ sang gốc mới đặt tại khối tâm G(a, b)"},
                {"step": "I_\\Delta = \\int [(x_i' + a)^2 + (y_i' + b)^2] dm = \\int (x_i'^2 + y_i'^2)dm + (a^2 + b^2)\\int dm + 2a\\int x_i' dm + 2b\\int y_i' dm", "reason": "Khai triển các hằng đẳng thức đáng nhớ"},
                {"step": "\\int x_i' dm = 0, \\quad \\int y_i' dm = 0", "reason": "Tọa độ khối tâm trong hệ quy chiếu gắn với chính khối tâm bằng 0"},
                {"step": "I_\\Delta = I_{cm} + m d^2", "reason": "Thu được định lý Steiner. Nhận xét: I_cm là momen quán tính nhỏ nhất trong mọi trục song song"}
            ]
        },
        {
            "name": "Chuyển động song phẳng và Lăn không trượt",
            "latex": "K = \\frac{1}{2}m v_{cm}^2 + \\frac{1}{2}I_{cm}\\omega^2; \\quad v_{cm} = \\omega R; \\quad a_{cm} = \\frac{g\\sin\\alpha}{1 + \\frac{I_{cm}}{m R^2}}",
            "meaning": "Vật lăn không trượt vừa tịnh tiến khối tâm vừa quay quanh khối tâm. Điểm tiếp xúc tức thời đứng yên nên lực ma sát nghỉ không sinh công, cơ năng được bảo toàn.",
            "proof": [
                {"step": "m a_{cm} = mg\\sin\\alpha - f_{ms}", "reason": "Định luật II Newton cho chuyển động tịnh tiến dọc theo mặt phẳng nghiêng"},
                {"step": "I_{cm}\\beta = f_{ms} R", "reason": "Phương trình chuyển động quay quanh trục đi qua khối tâm (chỉ có ma sát nghỉ tạo momen quay)"},
                {"step": "v_{cm} = \\omega R \\implies a_{cm} = \\beta R \\implies \\beta = \\frac{a_{cm}}{R}", "reason": "Điều kiện động học lăn không trượt"},
                {"step": "f_{ms} = \\frac{I_{cm}\\beta}{R} = \\frac{I_{cm} a_{cm}}{R^2}", "reason": "Rút lực ma sát nghỉ từ phương trình quay"},
                {"step": "m a_{cm} + \\frac{I_{cm}}{R^2}a_{cm} = mg\\sin\\alpha \\implies a_{cm} = \\frac{g\\sin\\alpha}{1 + \\frac{I_{cm}}{m R^2}}", "reason": "Thế lực ma sát vào phương trình tịnh tiến để giải ra gia tốc khối tâm"}
            ],
            "svg": '<svg viewBox="0 0 380 180" class="svg-diagram"><defs><marker id="arrV5" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#6366f1"/></marker><marker id="arrFms5" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/></marker></defs><line x1="20" y1="150" x2="340" y2="40" stroke="#94a3b8" stroke-width="2.5"/><polygon points="20,150 340,40 340,150" fill="rgba(148,163,184,0.1)"/><circle cx="180" cy="75" r="32" fill="#e2e8f0" stroke="#334155" stroke-width="2"/><circle cx="180" cy="75" r="4" fill="#6366f1"/><line x1="180" y1="75" x2="235" y2="55" stroke="#6366f1" stroke-width="3" marker-end="url(#arrV5)"/><text x="240" y="58" fill="#6366f1" font-weight="bold" font-size="12">v_cm</text><path d="M 195 60 A 20 20 0 0 1 190 95" fill="none" stroke="#10b981" stroke-width="2.5"/><text x="202" y="82" fill="#10b981" font-weight="bold" font-size="12">ω</text><line x1="168" y1="102" x2="120" y2="118" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrFms5)"/><text x="90" y="132" fill="#f59e0b" font-weight="bold" font-size="12">f_ms (nghỉ)</text><circle cx="168" cy="102" r="3" fill="#ef4444"/><text x="160" y="125" fill="#ef4444" font-size="11">Điểm tiếp xúc (v=0)</text></svg>'
        },
        {
            "name": "Định luật bảo toàn Momen động lượng trong Vật rắn",
            "latex": "\\sum M_z^{ng} = 0 \\implies L_z = I\\omega = \\text{const} \\implies I_1 \\omega_1 = I_2 \\omega_2",
            "meaning": "Nếu tổng momen ngoại lực đối với trục quay bằng 0 thì momen động lượng của vật rắn bảo toàn. Khi vật tự biến dạng để thu hẹp khối lượng về gần trục (I giảm), tốc độ quay $\\omega$ sẽ tự động tăng vọt (người trượt băng nghệ thuật xoay tít).",
            "proof": [
                {"step": "\\frac{dL_z}{dt} = M_z^{ng}", "reason": "Phương trình biến thiên momen động lượng"},
                {"step": "M_z^{ng} = 0 \\implies \\frac{dL_z}{dt} = 0 \\implies L_z = \\text{const}", "reason": "Lấy tích phân khi đạo hàm triệt tiêu"},
                {"step": "L_z = I_1 \\omega_1 = I_2 \\omega_2", "reason": "Tại hai trạng thái biến dạng cấu hình phân bố khối lượng khác nhau"},
                {"step": "K_2 = \\frac{L^2}{2I_2} > \\frac{L^2}{2I_1} = K_1 \\quad (\\text{khi } I_2 < I_1)", "reason": "Động năng tăng lên do công của cơ bắp người thực hiện chống lại lực quán tính ly tâm"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Tính Momen quán tính của vật đồng chất và áp dụng định lý Steiner",
            "algorithm": [
                "Bước 1: Tra cứu momen quán tính qua trục đối xứng khối tâm: Thanh mảnh ($I_{cm} = \\frac{1}{12}m\\ell^2$), đĩa/trụ đặc ($I_{cm} = \\frac{1}{2}mR^2$), cầu đặc ($I_{cm} = \\frac{2}{5}mR^2$), vành tròn ($I_{cm} = mR^2$).",
                "Bước 2: Xác định khoảng cách $d$ từ trục quay mới đến trục song song đi qua khối tâm.",
                "Bước 3: Áp dụng định lý Steiner: $I = I_{cm} + md^2$.",
                "Bước 4: Nếu là vật phẳng mỏng: Có thể dùng định lý trục vuông góc $I_z = I_x + I_y$."
            ]
        },
        {
            "name": "Dạng 2: Bài toán quay quanh trục cố định và ròng rọc có khối lượng (Máy Atwood thực)",
            "algorithm": [
                "Bước 1: Viết phương trình định luật II Newton cho các vật chuyển động tịnh tiến: $m_1 g - T_1 = m_1 a$, $T_2 - m_2 g = m_2 a$.",
                "Bước 2: Viết phương trình quay cho ròng rọc: $(T_1 - T_2)R = I\\beta = I\\frac{a}{R}$.",
                "Bước 3: Chú ý: Vì ròng rọc có khối lượng quán tính nên lực căng dây ở hai phía khác nhau ($T_1 \\ne T_2$).",
                "Bước 4: Cộng các phương trình để khử $T_1, T_2$ và giải tìm gia tốc $a = \\frac{(m_1 - m_2)g}{m_1 + m_2 + I/R^2}$."
            ]
        },
        {
            "name": "Dạng 3: Bài toán lăn không trượt trên mặt phẳng nghiêng",
            "algorithm": [
                "Bước 1: Thiết lập phương trình tịnh tiến: $mg\\sin\\alpha - f_{ms} = ma_{cm}$; và phương trình quay: $f_{ms} R = I_{cm}\\beta$.",
                "Bước 2: Dùng điều kiện lăn không trượt $a_{cm} = \\beta R$ để rút ra gia tốc $a_{cm} = \\frac{g\\sin\\alpha}{1 + I_{cm}/(mR^2)}$.",
                "Bước 3: Tính lực ma sát nghỉ cần thiết: $f_{ms} = m a_{cm} \\frac{I_{cm}}{mR^2}$.",
                "Bước 4: Đặt điều kiện không bị trượt: $f_{ms} \\le \\mu_s N = \\mu_s mg\\cos\\alpha \\implies \\mu_s \\ge \\tan\\alpha \\frac{k}{1+k}$."
            ]
        },
        {
            "name": "Dạng 4: Bảo toàn momen động lượng (Người xoay, va chạm vào vật gắn bản lề)",
            "algorithm": [
                "Bước 1: Kiểm tra ngoại lực có gây momen quanh trục quay không: Nếu $\\sum M_z^{ng} = 0$, áp dụng $I_1 \\omega_1 = I_2 \\omega_2$.",
                "Bước 2: Khi có chất điểm rơi vào hoặc bắn vào vật gắn trục quay: $L_{truoc} = I_{vat} \\omega_0 + m v_0 d$; $L_{sau} = (I_{vat} + m d^2)\\omega$.",
                "Bước 3: Giải tìm vận tốc góc $\\omega$ sau tương tác.",
                "Bước 4: Đánh giá độ biến thiên động năng: $\\Delta K = \\frac{1}{2}I_{sau}\\omega^2 - K_{truoc}$."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ 1: Máy Atwood có ròng rọc mang khối lượng (Ròng rọc thực)",
            "problem": "Một ròng rọc có dạng một đĩa tròn đặc đồng chất khối lượng $M = 2\\,\\text{kg}$, bán kính $R = 0.1\\,\\text{m}$. Hai vật có khối lượng $m_1 = 3\\,\\text{kg}$ và $m_2 = 1\\,\\text{kg}$ được nối bằng sợi dây nhẹ không dãn vắt qua ròng rọc. Dây không trượt trên ròng rọc. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính gia tốc của các vật và lực căng của dây ở mỗi nhánh.",
            "analysis": "Ròng rọc là đĩa đặc nên có momen quán tính $I = \\frac{1}{2}MR^2$. Dây không trượt làm ròng rọc quay với gia tốc góc $\\beta = a/R$. Lực căng ở hai nhánh dây không bằng nhau vì hiệu lực căng $(T_1 - T_2)$ sinh ra momen làm quay ròng rọc.",
            "solution": "1. Momen quán tính của ròng rọc:\\n$$I = \\frac{1}{2}M R^2 = \\frac{1}{2}(2)(0.1)^2 = 0.01\\,\\text{kg}\\cdot\\text{m}^2$$\\n\\n2. Thiết lập hệ phương trình động lực học:\\n- Vật 1 đi xuống: $m_1 g - T_1 = m_1 a \\quad (1)$\\n- Vật 2 đi lên: $T_2 - m_2 g = m_2 a \\quad (2)$\\n- Ròng rọc quay: $(T_1 - T_2)R = I\\beta = I\\frac{a}{R} \\implies T_1 - T_2 = \\frac{I}{R^2}a = \\frac{1}{2}M a \\quad (3)$\\n\\n3. Cộng (1), (2) và (3) để khử $T_1$ và $T_2$:\\n$$(m_1 - m_2)g = \\left(m_1 + m_2 + \\frac{1}{2}M\\right)a$$\\n$$a = \\frac{(m_1 - m_2)g}{m_1 + m_2 + M/2}$$\\nThay số:\\n$$a = \\frac{(3 - 1) \\times 9.8}{3 + 1 + 2/2} = \\frac{2 \\times 9.8}{5} = \\frac{19.6}{5} = 3.92\\,\\text{m/s}^2$$\\n\\n4. Tính lực căng ở mỗi nhánh dây:\\n- Nhánh 1: $T_1 = m_1(g - a) = 3 \\times (9.8 - 3.92) = 3 \\times 5.88 = 17.64\\,\\text{N}$\\n- Nhánh 2: $T_2 = m_2(g + a) = 1 \\times (9.8 + 3.92) = 13.72\\,\\text{N}$\\n(Kiểm tra: $T_1 - T_2 = 17.64 - 13.72 = 3.92\\,\\text{N} = \\frac{1}{2}M a = \\frac{1}{2}(2)(3.92) = 3.92\\,\\text{N}$ chuẩn xác)."
        },
        {
            "title": "Ví dụ 2: Thanh đồng chất đổ quanh bản lề",
            "problem": "Một thanh mảnh đồng chất chiều dài $\\ell = 1.5\\,\\text{m}$, khối lượng $m = 2\\,\\text{kg}$ có một đầu gắn vào bản lề cố định tại $O$. Thanh được thả rơi tự do không vận tốc đầu từ vị trí nằm ngang. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính gia tốc góc ban đầu $\\beta_0$ và vận tốc dài của đầu tự do khi thanh đi qua vị trí thẳng đứng.",
            "analysis": "Tại vị trí nằm ngang, trọng lực tác dụng tại khối tâm (cách O một đoạn $\\ell/2$) tạo momen quay. Khi thanh rơi xuống vị trí thẳng đứng, áp dụng định luật bảo toàn cơ năng.",
            "solution": "1. Momen quán tính của thanh quanh trục đi qua đầu thanh:\\n$$I_O = \\frac{1}{3}m\\ell^2$$\\n2. Gia tốc góc ban đầu khi thanh nằm ngang:\\nMomen trọng lực: $M = mg \\frac{\\ell}{2}$.\\n$$\\beta_0 = \\frac{M}{I_O} = \\frac{mg\\ell/2}{\\frac{1}{3}m\\ell^2} = \\frac{3g}{2\\ell} = \\frac{3 \\times 9.8}{2 \\times 1.5} = \\frac{29.4}{3.0} = 9.8\\,\\text{rad/s}^2$$\\n\\n3. Vận tốc góc khi qua vị trí thẳng đứng:\\nChọn mốc thế năng tại vị trí thấp nhất của khối tâm khi thanh thẳng đứng.\\n- Độ giảm thế năng của khối tâm: $\\Delta U = mg \\frac{\\ell}{2}$.\\n- Toàn bộ thế năng chuyển thành động năng quay:\\n$$\\Delta U = \\frac{1}{2}I_O \\omega^2 \\iff mg\\frac{\\ell}{2} = \\frac{1}{2}\\left(\\frac{1}{3}m\\ell^2\\right)\\omega^2$$\\n$$\\omega^2 = \\frac{3g}{\\ell} \\implies \\omega = \\sqrt{\\frac{3g}{\\ell}}$$\\n4. Vận tốc dài của đầu tự do của thanh:\\n$$v = \\omega \\ell = \\sqrt{\\frac{3g}{\\ell}} \\times \\ell = \\sqrt{3g\\ell}$$\\nThay số:\\n$$v = \\sqrt{3 \\times 9.8 \\times 1.5} = \\sqrt{44.1} \\approx 6.64\\,\\text{m/s}$$\\n(So sánh: Vận tốc rơi tự do của một chất điểm từ cùng độ cao $\\ell$ chỉ là $v_{roi} = \\sqrt{2g\\ell} = \\sqrt{29.4} \\approx 5.42\\,\\text{m/s}$. Đầu thanh quay nhanh hơn rơi tự do vì các phần tử phía trong truyền lực kéo phần tử phía ngoài!)."
        }
    ],
    "pitfalls": [
        {
            "error": "Tự ý sử dụng v = ωR khi vật đang trượt",
            "fix": "Hệ thức $v = \\omega R$ và $a = \\beta R$ CHỈ đúng khi vật lăn hoàn toàn không trượt. Nếu bánh xe bị bó cứng khi phanh hoặc quay tít trên bùn lầy (lăn có trượt) thì $v \\ne \\omega R$.",
            "tip": "Khi bài toán cho 'lăn có trượt', lực ma sát là ma sát trượt $F_{mst} = \\mu_k N$ và hai phương trình tịnh tiến - quay hoàn toàn độc lập."
        },
        {
            "error": "Quên số hạng động năng quay trong chuyển động lăn không trượt",
            "fix": "Động năng của vật lăn không trượt gồm cả hai phần: $K = \\frac{1}{2}m v_{cm}^2 + \\frac{1}{2}I_{cm}\\omega^2$. Nếu bỏ quên phần quay sẽ dẫn đến tính toán vận tốc sai nghiêm trọng.",
            "tip": "Với cầu đặc, $K = \\frac{1}{2}mv^2(1 + 2/5) = \\frac{7}{10}mv^2$. Với trụ đặc, $K = \\frac{1}{2}mv^2(1 + 1/2) = \\frac{3}{4}mv^2$."
        },
        {
            "error": "Áp dụng định lý Steiner sai chiều: lấy I_cm = I + md² thay vì I = I_cm + md²",
            "fix": "Momen quán tính đối với trục qua khối tâm $I_{cm}$ luôn luôn là giá trị nhỏ nhất trong mọi trục song song. Mọi trục quay lệch tâm đều có $I > I_{cm}$.",
            "tip": "Hãy luôn nhớ dấu cộng: $I = I_{cm} + md^2$."
        }
    ],
    "exercises": [
        {
            "id": "ex_5_1",
            "type": "easy",
            "q": "Một công nhân dùng mỏ lết dài $d = 0.25\\,\\text{m}$ để vặn một đai ốc. Người đó tác dụng một lực vuông góc với cán mỏ lết có độ lớn $F = 40\\,\\text{N}$. Hãy tính độ lớn momen lực tác dụng lên đai ốc đối với trục quay.",
            "unit": "N·m",
            "ans": 10.0,
            "tol": 0.05,
            "hints": [
                "Vì lực vuông góc với cánh tay đòn nên $\\sin 90^\\circ = 1$.",
                "Áp dụng công thức momen lực: $M = F \\times d$."
            ],
            "solution": "Độ lớn momen lực tác dụng lên đai ốc:\\n$$M = F \\times d = 40 \\times 0.25 = 10.0\\,\\text{N}\\cdot\\text{m}$$\\nĐáp số: 10.0 N·m"
        },
        {
            "id": "ex_5_2",
            "type": "easy",
            "q": "Một thanh đồng chất mảnh có chiều dài $\\ell = 1.2\\,\\text{m}$ và khối lượng $m = 2.5\\,\\text{kg}$. Hãy tính momen quán tính của thanh đối với trục quay vuông góc với thanh và đi qua trung điểm của nó.",
            "unit": "kg·m²",
            "ans": 0.3,
            "tol": 0.05,
            "hints": [
                "Momen quán tính của thanh mảnh qua khối tâm ở trung điểm: $I = \\frac{1}{12}m\\ell^2$.",
                "Thay $m = 2.5\\,\\text{kg}$ và $\\ell = 1.2\\,\\text{m}$."
            ],
            "solution": "Áp dụng công thức momen quán tính của thanh mảnh:\\n$$I = \\frac{1}{12}m\\ell^2 = \\frac{1}{12} \\times 2.5 \\times (1.2)^2 = \\frac{1}{12} \\times 2.5 \\times 1.44 = \\frac{3.6}{12} = 0.3\\,\\text{kg}\\cdot\\text{m}^2$$\\nĐáp số: 0.3 kg·m²"
        },
        {
            "id": "ex_5_3",
            "type": "easy",
            "q": "Một bánh đà có momen quán tính $I = 0.5\\,\\text{kg}\\cdot\\text{m}^2$ chịu tác dụng của một momen lực cản không đổi $M = 4.0\\,\\text{N}\\cdot\\text{m}$. Hãy tính độ lớn gia tốc góc hãm của bánh đà.",
            "unit": "rad/s²",
            "ans": 8.0,
            "tol": 0.05,
            "hints": [
                "Phương trình cơ bản của chuyển động quay quanh trục cố định: $M = I\\beta$.",
                "Gia tốc góc: $\\beta = M / I$."
            ],
            "solution": "Theo phương trình cơ bản của chuyển động quay:\\n$$M = I\\beta \\implies \\beta = \\frac{M}{I} = \\frac{4.0}{0.5} = 8.0\\,\\text{rad/s}^2$$\\nĐáp số: 8.0 rad/s²"
        },
        {
            "id": "ex_5_4",
            "type": "easy",
            "q": "Một bánh xe có momen quán tính đối với trục quay là $I = 0.8\\,\\text{kg}\\cdot\\text{m}^2$ đang quay đều với tốc độ góc $\\omega = 15\\,\\text{rad/s}$. Hãy tính động năng quay của bánh xe theo đơn vị Jun (J).",
            "unit": "J",
            "ans": 90.0,
            "tol": 0.05,
            "hints": [
                "Công thức tính động năng chuyển động quay: $K = \\frac{1}{2}I\\omega^2$.",
                "Thay các giá trị $I = 0.8$ và $\\omega = 15$."
            ],
            "solution": "Áp dụng công thức động năng quay:\\n$$K = \\frac{1}{2}I\\omega^2 = \\frac{1}{2} \\times 0.8 \\times 15^2 = 0.4 \\times 225 = 90.0\\,\\text{J}$$\\nĐáp số: 90.0 J"
        },
        {
            "id": "ex_5_5",
            "type": "mid",
            "q": "Một thanh đồng chất mảnh có khối lượng $m = 3\\,\\text{kg}$ và chiều dài $\\ell = 2\\,\\text{m}$. Hãy tính momen quán tính của thanh đối với trục quay vuông góc với thanh và đi qua điểm cách một đầu thanh một đoạn $0.5\\,\\text{m}$ (làm tròn đến 2 chữ số thập phân).",
            "unit": "kg·m²",
            "ans": 1.75,
            "tol": 0.05,
            "hints": [
                "Khối tâm thanh ở trung điểm cách đầu thanh $1.0\\,\\text{m}$.",
                "Khoảng cách giữa trục quay mới và khối tâm là $d = 1.0 - 0.5 = 0.5\\,\\text{m}$.",
                "Áp dụng định lý Steiner: $I = I_{cm} + md^2 = \\frac{1}{12}m\\ell^2 + md^2$."
            ],
            "solution": "1. Momen quán tính đối với trục đi qua khối tâm (trung điểm thanh):\\n$$I_{cm} = \\frac{1}{12}m\\ell^2 = \\frac{1}{12} \\times 3 \\times 2^2 = \\frac{12}{12} = 1.0\\,\\text{kg}\\cdot\\text{m}^2$$\\n2. Khoảng cách từ trục quay đến khối tâm:\\n$$d = \\frac{\\ell}{2} - 0.5 = 1.0 - 0.5 = 0.5\\,\\text{m}$$\\n3. Áp dụng định lý Steiner:\\n$$I = I_{cm} + m d^2 = 1.0 + 3 \\times (0.5)^2 = 1.0 + 3 \\times 0.25 = 1.0 + 0.75 = 1.75\\,\\text{kg}\\cdot\\text{m}^2$$\\nĐáp số: 1.75 kg·m²"
        },
        {
            "id": "ex_5_6",
            "type": "mid",
            "q": "Trong máy Atwood có xét đến khối lượng ròng rọc: Ròng rọc là một đĩa đặc đồng chất có khối lượng $M = 2\\,\\text{kg}$, bán kính $R = 0.1\\,\\text{m}$ ($I = \\frac{1}{2}MR^2$). Hai vật có khối lượng $m_1 = 3\\,\\text{kg}$ và $m_2 = 1\\,\\text{kg}$ nối với nhau qua ròng rọc bằng dây nhẹ không trượt. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính gia tốc chuyển động của hệ hai vật (m/s²).",
            "unit": "m/s²",
            "ans": 3.92,
            "tol": 0.05,
            "hints": [
                "Gia tốc của hệ khi ròng rọc có khối lượng $M$: $a = \\frac{(m_1 - m_2)g}{m_1 + m_2 + M/2}$.",
                "Thay số: $m_1 = 3, m_2 = 1, M = 2, g = 9.8$."
            ],
            "solution": "Áp dụng công thức gia tốc cho máy Atwood có ròng rọc đĩa đặc:\\n$$a = \\frac{(m_1 - m_2)g}{m_1 + m_2 + \\frac{1}{2}M}$$\\nThay các giá trị số:\\n$$a = \\frac{(3 - 1) \\times 9.8}{3 + 1 + \\frac{1}{2}(2)} = \\frac{2 \\times 9.8}{3 + 1 + 1} = \\frac{19.6}{5} = 3.92\\,\\text{m/s}^2$$\\nĐáp số: 3.92 m/s²"
        },
        {
            "id": "ex_5_7",
            "type": "mid",
            "q": "Một khối cầu đặc đồng chất ($I_{cm} = \\frac{2}{5}mR^2$) lăn không trượt xuống một mặt dốc nghiêng góc $\\alpha = 30^\\circ$ so với phương ngang. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính gia tốc tịnh tiến của khối tâm quả cầu.",
            "unit": "m/s²",
            "ans": 3.5,
            "tol": 0.05,
            "hints": [
                "Công thức gia tốc khối tâm khi lăn không trượt: $a_{cm} = \\frac{g\\sin\\alpha}{1 + I_{cm}/(mR^2)}$.",
                "Với cầu đặc, tỉ số $I_{cm}/(mR^2) = 2/5 = 0.4$.",
                "Mẫu số là $1 + 0.4 = 1.4 = 7/5$."
            ],
            "solution": "Áp dụng công thức gia tốc lăn không trượt cho khối cầu đặc:\\n$$a_{cm} = \\frac{g\\sin\\alpha}{1 + \\frac{2}{5}} = \\frac{5}{7}g\\sin\\alpha$$\\nThay $\\alpha = 30^\\circ$ ($\\sin 30^\\circ = 0.5$) và $g = 9.8\\,\\text{m/s}^2$:\\n$$a_{cm} = \\frac{5}{7} \\times 9.8 \\times 0.5 = \\frac{5}{7} \\times 4.9 = 5 \\times 0.7 = 3.5\\,\\text{m/s}^2$$\\nĐáp số: 3.5 m/s²"
        },
        {
            "id": "ex_5_8",
            "type": "mid",
            "q": "Một nghệ sĩ trượt băng đang thực hiện động tác xoay với hai tay giang rộng có momen quán tính $I_1 = 2.4\\,\\text{kg}\\cdot\\text{m}^2$ và tốc độ góc quay $\\omega_1 = 2.0\\,\\text{vòng/giây}$. Khi người đó co hai tay lại sát thân người, momen quán tính giảm xuống còn $I_2 = 0.8\\,\\text{kg}\\cdot\\text{m}^2$. Bỏ qua ma sát với mặt băng. Hãy tính tốc độ góc quay mới $\\omega_2$ của nghệ sĩ theo đơn vị vòng/giây.",
            "unit": "vòng/s",
            "ans": 6.0,
            "tol": 0.05,
            "hints": [
                "Do không có ngoại lực gây momen quanh trục quay thẳng đứng nên momen động lượng bảo toàn:",
                "$I_1 \\omega_1 = I_2 \\omega_2 \\implies \\omega_2 = \\frac{I_1 \\omega_1}{I_2}$."
            ],
            "solution": "Áp dụng định luật bảo toàn momen động lượng cho hệ kín quay quanh trục thẳng đứng:\\n$$L_1 = L_2 \\iff I_1 \\omega_1 = I_2 \\omega_2$$\\nTốc độ góc mới của nghệ sĩ:\\n$$\\omega_2 = \\frac{I_1 \\omega_1}{I_2} = \\frac{2.4 \\times 2.0}{0.8} = 3 \\times 2.0 = 6.0\\,\\text{vòng/giây}$$\\nĐáp số: 6.0 vòng/s"
        },
        {
            "id": "ex_5_9",
            "type": "hard",
            "q": "Một thanh mảnh đồng chất có chiều dài $\\ell = 1.5\\,\\text{m}$ có một đầu được giữ bởi bản lề không ma sát tại O. Thanh được thả không vận tốc đầu từ vị trí nằm ngang. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính vận tốc dài của đầu mút tự do của thanh tại thời điểm thanh đi qua vị trí thẳng đứng (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s",
            "ans": 6.64,
            "tol": 0.1,
            "hints": [
                "Momen quán tính của thanh qua đầu bản lề: $I_O = \\frac{1}{3}m\\ell^2$.",
                "Độ giảm thế năng của khối tâm: $\\Delta U = mg \\frac{\\ell}{2}$.",
                "Bảo toàn cơ năng: $mg\\frac{\\ell}{2} = \\frac{1}{2}I_O \\omega^2 \\implies \\omega = \\sqrt{\\frac{3g}{\\ell}}$.",
                "Vận tốc dài của đầu mút thanh: $v = \\omega \\ell = \\sqrt{3g\\ell}$."
            ],
            "solution": "1. Momen quán tính của thanh quanh trục đi qua một đầu:\\n$$I_O = \\frac{1}{3}m\\ell^2$$\\n2. Bảo toàn cơ năng khi khối tâm hạ xuống một đoạn $h = \\ell/2$:\\n$$mg\\frac{\\ell}{2} = \\frac{1}{2}I_O \\omega^2 \\iff mg\\frac{\\ell}{2} = \\frac{1}{2}\\left(\\frac{1}{3}m\\ell^2\\right)\\omega^2$$\\n$$\\omega = \\sqrt{\\frac{3g}{\\ell}}$$\\n3. Vận tốc dài của đầu tự do của thanh:\\n$$v = \\omega \\ell = \\sqrt{3g\\ell}$$\\nThay các giá trị số:\\n$$v = \\sqrt{3 \\times 9.8 \\times 1.5} = \\sqrt{44.1} \\approx 6.6408 \\approx 6.64\\,\\text{m/s}$$\\nĐáp số: 6.64 m/s"
        },
        {
            "id": "ex_5_10",
            "type": "hard",
            "q": "Một hình trụ đặc đồng chất ($I_{cm} = \\frac{1}{2}mR^2$) được đặt trên mặt phẳng nghiêng góc $\\alpha = 45^\\circ$ so với phương ngang. Để hình trụ có thể lăn hoàn toàn không trượt xuống dốc thì hệ số ma sát nghỉ tối thiểu $\\mu_{s\\,\\min}$ giữa hình trụ và mặt phẳng nghiêng phải bằng bao nhiêu? (Làm tròn đến 2 chữ số thập phân).",
            "unit": "",
            "ans": 0.33,
            "tol": 0.05,
            "hints": [
                "Lực ma sát nghỉ cần thiết để lăn không trượt: $f_{ms} = mg\\sin\\alpha \\frac{k}{1+k}$ với $k = \\frac{I_{cm}}{mR^2} = \\frac{1}{2}$.",
                "Điều kiện không trượt là $f_{ms} \\le \\mu_s N = \\mu_s mg\\cos\\alpha$.",
                "Suy ra $\\mu_{s\\,\\min} = \\tan\\alpha \\frac{k}{1+k} = \\tan 45^\\circ \\times \\frac{1/2}{1 + 1/2} = \\frac{1}{3}$."
            ],
            "solution": "1. Phương trình động lực học cho chuyển động tịnh tiến và quay:\\n- Tịnh tiến: $mg\\sin\\alpha - f_{ms} = ma_{cm}$\\n- Quay quanh khối tâm: $f_{ms} R = I_{cm}\\beta = \\left(\\frac{1}{2}mR^2\\right)\\frac{a_{cm}}{R} \\implies f_{ms} = \\frac{1}{2}m a_{cm}$\\n2. Thay vào phương trình tịnh tiến:\\n$$ma_{cm} + \\frac{1}{2}ma_{cm} = mg\\sin\\alpha \\implies a_{cm} = \\frac{2}{3}g\\sin\\alpha$$\\n$$f_{ms} = \\frac{1}{2}m\\left(\\frac{2}{3}g\\sin\\alpha\\right) = \\frac{1}{3}mg\\sin\\alpha$$\\n3. Điều kiện để không trượt ($f_{ms} \\le \\mu_s N$ với $N = mg\\cos\\alpha$):\\n$$\\frac{1}{3}mg\\sin\\alpha \\le \\mu_s mg\\cos\\alpha \\implies \\mu_s \\ge \\frac{1}{3}\\tan\\alpha$$\\nVới $\\alpha = 45^\\circ$ thì $\\tan 45^\\circ = 1$:\\n$$\\mu_{s\\,\\min} = \\frac{1}{3} \\approx 0.3333 \\approx 0.33$$\\nĐáp số: 0.33"
        }
    ]
}

print("Chapter 5 data module ready.")
