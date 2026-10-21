# -*- coding: utf-8 -*-
"""
Module defining chapter 2 data: Động lực học chất điểm
"""

CH2 = {
    "id": 2,
    "num": 2,
    "part": "Phần I — Cơ học",
    "title": "Động lực học chất điểm",
    "tag": "Ba định luật Newton & Các lực cơ bản",
    "status": "ready",
    "summary": "Nghiên cứu nguyên nhân làm thay đổi trạng thái chuyển động: Ba định luật Newton, các lực cơ bản trong tự nhiên (trọng lực, ma sát, đàn hồi, phản lực), lực hướng tâm, lực cản môi trường và lực quán tính.",
    "nature": {
        "why": "Động học chỉ trả lời câu hỏi 'chuyển động như thế nào?', còn động lực học trả lời câu hỏi căn bản 'tại sao vật lại chuyển động biến đổi?'. Lực là đại lượng vật lý đặc trưng cho tác dụng tương hỗ giữa các vật, là nguyên nhân làm biến đổi vận tốc (tạo ra gia tốc) hoặc làm biến dạng vật.",
        "meaning": "Định luật I khẳng định sự tồn tại của hệ quy chiếu quán tính (vật cô lập giữ nguyên trạng thái đứng yên hoặc chuyển động thẳng đều nhờ quán tính). Định luật II xác lập mối quan hệ nhân - quả định lượng: Hợp lực là nguyên nhân, gia tốc là kết quả tỷ lệ nghịch với khối lượng quán tính $m$. Định luật III phản ánh tính đối xứng của tự nhiên: Mọi lực đều xuất hiện theo từng cặp tương tác trực đối đặt vào hai vật khác nhau. Lực quán tính trong hệ phi quán tính là lực ảo xuất hiện do chính gia tốc của hệ quy chiếu quan sát.",
        "conditions": "Ba định luật Newton chỉ nghiệm đúng tuyệt đối trong Hệ quy chiếu quán tính (hệ gắn với các ngôi sao ở xa hoặc Trái Đất khi bỏ qua chuyển động tự quay). Tốc độ của vật phải nhỏ hơn rất nhiều so với tốc độ ánh sáng ($v \\ll c$).",
        "limits": "Khi chuyển động trong hệ quy chiếu phi quán tính (như ôtô phanh gấp, thang máy tăng tốc, đĩa quay), phải bổ sung thêm các lực quán tính (lực tịnh tiến, lực ly tâm, lực Coriolis) thì định luật II mới áp dụng được. Ở cấp độ vi mô nguyên tử, cơ học Newton phải nhường chỗ cho Cơ học lượng tử."
    },
    "formulas": [
        {
            "name": "Ba định luật cơ bản của Newton",
            "latex": "\\text{ĐL I: } \\sum \\vec{F} = \\vec{0} \\iff \\vec{v} = \\text{const}; \\quad \\text{ĐL II: } \\vec{F} = \\frac{d\\vec{p}}{dt} = m\\vec{a}; \\quad \\text{ĐL III: } \\vec{F}_{12} = -\\vec{F}_{21}",
            "meaning": "Ba định luật nền tảng của toàn bộ cơ học cổ điển. Động lượng $\\vec{p} = m\\vec{v}$ là đại lượng đo lượng chuyển động cơ học.",
            "proof": [
                {"step": "\\vec{p} = m\\vec{v}", "reason": "Định nghĩa vectơ động lượng của chất điểm"},
                {"step": "\\vec{F} = \\frac{d\\vec{p}}{dt} = \\frac{d(m\\vec{v})}{dt}", "reason": "Phát biểu nguyên bản của Newton: Lực là tốc độ biến thiên của động lượng theo thời gian"},
                {"step": "\\vec{F} = \\frac{dm}{dt}\\vec{v} + m\\frac{d\\vec{v}}{dt}", "reason": "Đạo hàm của tích hàm số theo thời gian"},
                {"step": "\\frac{dm}{dt} = 0 \\implies \\vec{F} = m\\frac{d\\vec{v}}{dt} = m\\vec{a}", "reason": "Trong cơ học cổ điển, khối lượng chất điểm là hằng số bất biến đối với thời gian"},
                {"step": "\\vec{F}_{12} + \\vec{F}_{21} = \\vec{0} \\implies \\frac{d\\vec{p}_1}{dt} + \\frac{d\\vec{p}_2}{dt} = \\vec{0}", "reason": "Định luật III dẫn trực tiếp đến định luật bảo toàn tổng động lượng của hệ cô lập"}
            ]
        },
        {
            "name": "Định luật ma sát Amontons - Coulomb",
            "latex": "F_{msn} \\le F_{msn\\,\\max} = \\mu_s N; \\quad F_{mst} = \\mu_k N",
            "meaning": "Lực ma sát nghỉ tự động điều chỉnh độ lớn để cân bằng với ngoại lực giữ vật đứng yên; khi ngoại lực vượt ngưỡng cực đại $\\mu_s N$, vật bắt đầu trượt và ma sát chuyển thành ma sát trượt có độ lớn tỷ lệ thuận với áp lực pháp tuyến $N$ (thông thường $\\mu_k \\le \\mu_s$).",
            "proof": [
                {"step": "\\sum \\vec{F}_x = \\vec{F}_{keo} + \\vec{F}_{msn} = \\vec{0}", "reason": "Khi vật vẫn đứng yên cân bằng trên mặt tiếp xúc (gia tốc a = 0)"},
                {"step": "F_{msn} = F_{keo}", "reason": "Độ lớn ma sát nghỉ bằng đúng ngoại lực tiếp tuyến tác dụng"},
                {"step": "F_{msn\\,\\max} = \\mu_s N", "reason": "Thực nghiệm Coulomb: Giới hạn bứt phá của các liên kết vi mô tỷ lệ với lực ép hai bề mặt"},
                {"step": "F_{keo} > \\mu_s N \\implies F_{mst} = \\mu_k N", "reason": "Khi các đỉnh nhấp nhô tế vi bị san phẳng và trượt lướt qua nhau"}
            ],
            "svg": '<svg viewBox="0 0 380 180" class="svg-diagram"><defs><marker id="arrF" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#6366f1"/></marker><marker id="arrN" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/></marker><marker id="arrP" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/></marker><marker id="arrMs" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/></marker></defs><line x1="20" y1="140" x2="320" y2="40" stroke="#94a3b8" stroke-width="2.5"/><polygon points="20,140 320,40 320,140" fill="rgba(148,163,184,0.1)"/><rect x="150" y="70" width="50" height="30" transform="rotate(-18.4, 175, 85)" fill="#e2e8f0" stroke="#475569" stroke-width="2"/><line x1="175" y1="85" x2="175" y2="165" stroke="#ef4444" stroke-width="3" marker-end="url(#arrP)"/><text x="180" y="160" fill="#ef4444" font-weight="bold" font-size="12">P = mg</text><line x1="175" y1="85" x2="200" y2="10" stroke="#10b981" stroke-width="3" marker-end="url(#arrN)"/><text x="205" y="20" fill="#10b981" font-weight="bold" font-size="12">N</text><line x1="175" y1="85" x2="110" y2="107" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrMs)"/><text x="80" y="125" fill="#f59e0b" font-weight="bold" font-size="12">F_ms</text></svg>'
        },
        {
            "name": "Phương trình vi phân rơi có lực cản môi trường tỷ lệ bậc nhất vận tốc",
            "latex": "m\\frac{dv}{dt} = mg - kv \\implies v(t) = v_{lim}\\left(1 - e^{-\\frac{k}{m}t}\\right); \\quad v_{lim} = \\frac{mg}{k}",
            "meaning": "Mô tả hạt bụi, giọt sương hoặc vật nhỏ rơi trong chất lưu nhớt (lực cản Stokes $F_c = -kv$). Vận tốc tăng dần và tiệm cận đến vận tốc tới hạn $v_{lim}$ khi lực cản cân bằng với trọng lực.",
            "proof": [
                {"step": "m\\frac{dv}{dt} = mg - kv \\implies \\frac{dv}{g - \\frac{k}{m}v} = dt", "reason": "Phân ly biến số trong phương trình vi phân cấp 1 tuyến tính"},
                {"step": "\\int_0^v \\frac{dv'}{1 - \\frac{k}{mg}v'} = g \\int_0^t dt' = gt", "reason": "Đặt nhân tử chung g ở mẫu số và lấy tích phân từ trạng thái nghỉ v(0) = 0"},
                {"step": "-\\frac{mg}{k} \\ln\\left(1 - \\frac{k}{mg}v\\right) = gt \\implies \\ln\\left(1 - \\frac{k}{mg}v\\right) = -\\frac{k}{m}t", "reason": "Áp dụng công thức nguyên hàm d(1 - ax)/ (1 - ax) = -a ln(1 - ax)"},
                {"step": "1 - \\frac{k}{mg}v = e^{-\\frac{k}{m}t} \\implies v(t) = \\frac{mg}{k}\\left(1 - e^{-\\frac{k}{m}t}\\right)", "reason": "Lấy hàm mũ hai vế và giải ra biểu thức vận tốc theo thời gian t"}
            ]
        },
        {
            "name": "Hệ quy chiếu phi quán tính và Lực quán tính",
            "latex": "\\vec{F}_{qt} = -m\\vec{a}_0; \\quad \\vec{F}_{lt} = m\\omega^2\\vec{r}; \\quad \\vec{F}_{Cor} = 2m(\\vec{v}' \\times \\vec{\\omega})",
            "meaning": "Khi quan sát chuyển động từ hệ quy chiếu có gia tốc $\\vec{a}_0$ (hệ phi quán tính), ta phải thêm lực quán tính $\\vec{F}_{qt} = -m\\vec{a}_0$ vào phương trình định luật II để thu được định luật dạng Newton: $\\sum \\vec{F}_{thuc} + \\vec{F}_{qt} = m\\vec{a}'$.",
            "proof": [
                {"step": "\\vec{r} = \\vec{R}_0 + \\vec{r}'", "reason": "Quan hệ vị trí giữa hệ quán tính K và hệ phi quán tính K'"},
                {"step": "\\frac{d^2\\vec{r}}{dt^2} = \\frac{d^2\\vec{R}_0}{dt^2} + \\frac{d^2\\vec{r}'}{dt^2} \\implies \\vec{a} = \\vec{a}_0 + \\vec{a}'", "reason": "Lấy đạo hàm cấp hai theo thời gian (giả sử hệ K' chỉ tịnh tiến gia tốc a₀)"},
                {"step": "m\\vec{a} = \\sum \\vec{F}_{thuc} \\implies m(\\vec{a}_0 + \\vec{a}') = \\sum \\vec{F}_{thuc}", "reason": "Áp dụng định luật II Newton đúng trong hệ quán tính K"},
                {"step": "m\\vec{a}' = \\sum \\vec{F}_{thuc} - m\\vec{a}_0 = \\sum \\vec{F}_{thuc} + \\vec{F}_{qt}", "reason": "Chuyển vế đặt F_qt = -m a₀ để phương trình trong hệ K' có dạng tựa Newton"}
            ]
        }
    ],
    "types": [
        {
            "name": "Dạng 1: Chuyển động của một vật hoặc hệ vật dưới tác dụng của các lực cơ bản",
            "algorithm": [
                "Bước 1: Vẽ biểu đồ vật tự do (FBD - Free Body Diagram): Liệt kê và biểu diễn tất cả các lực thực tế tác dụng lên từng vật (Trọng lực $\\vec{P}$, phản lực $\\vec{N}$, lực kéo $\\vec{F}_k$, ma sát $\\vec{F}_{ms}$, lực căng dây $\\vec{T}$).",
                "Bước 2: Chọn hệ trục tọa độ vuông góc thích hợp: Thường chọn trục $Ox$ song song với chiều chuyển động của vật, trục $Oy$ vuông góc với quỹ đạo.",
                "Bước 3: Viết phương trình vectơ định luật II Newton: $\\sum \\vec{F} = m\\vec{a}$.",
                "Bước 4: Chiếu phương trình lên hai trục: $Oy \\implies \\sum F_y = 0$ để tìm phản lực $N$ (từ đó tính $F_{ms} = \\mu N$); $Ox \\implies \\sum F_x = ma$ để tìm gia tốc $a$ và các lực liên kết."
            ]
        },
        {
            "name": "Dạng 2: Bài toán chuyển động tròn và lực hướng tâm",
            "algorithm": [
                "Bước 1: Xác định mặt phẳng quỹ đạo tròn, tâm quay $O$ và bán kính quay $R$.",
                "Bước 2: Biểu diễn các lực thực tế tác dụng lên vật. Chọn trục $On$ hướng về tâm quỹ đạo.",
                "Bước 3: Chiếu hợp lực lên phương hướng tâm: $F_n = m a_n = m\\frac{v^2}{R} = m\\omega^2 R$.",
                "Bước 4: Xác định điều kiện biên đặc biệt (ví dụ: vật qua đỉnh vòng xiếc không rơi khi phản lực $N \\ge 0$, ô tô vào cua không trượt khi $F_n \\le F_{msn\\,\\max}$)."
            ]
        },
        {
            "name": "Dạng 3: Bài toán trong hệ quy chiếu phi quán tính (Thang máy, xe gia tốc)",
            "algorithm": [
                "Bước 1: Xác định gia tốc $\\vec{a}_0$ của hệ quy chiếu chuyển động so với mặt đất.",
                "Bước 2: Gắn hệ quy chiếu vào vật chuyển động (như cabin thang máy hoặc xe), thêm lực quán tính $\\vec{F}_{qt} = -m\\vec{a}_0$ (luôn ngược hướng với gia tốc $\\vec{a}_0$).",
                "Bước 3: Thiết lập phương trình cân bằng hoặc chuyển động tương đối: $\\sum \\vec{F}_{thuc} + \\vec{F}_{qt} = m\\vec{a}'$.",
                "Bước 4: Tìm số chỉ của lực kế/cân (chính là độ lớn của phản lực $N$ hoặc lực căng dây $T$)."
            ]
        }
    ],
    "examples": [
        {
            "title": "Ví dụ 1: Tính góc nghiêng an toàn tối ưu cho khúc cua đường cao tốc",
            "problem": "Một khúc cua trên đường cao tốc có bán kính cong $R = 200\\,\\text{m}$. Mặt đường được thiết kế nghiêng vào phía trong một góc $\\alpha$ so với phương ngang để ô tô có thể chạy an toàn với vận tốc thiết kế $v = 72\\,\\text{km/h}$ ngay cả khi mặt đường đóng băng trơn trượt (hệ số ma sát coi như bằng 0). Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính góc nghiêng $\\alpha$.",
            "analysis": "Khi không có ma sát, chỉ có hai lực tác dụng lên ô tô: Trọng lực $\\vec{P}$ thẳng đứng hướng xuống và phản lực pháp tuyến $\\vec{N}$ vuông góc với mặt đường nghiêng. Thành phần nằm ngang của phản lực $\\vec{N}$ đóng vai trò là lực hướng tâm giữ cho xe vào cua.",
            "solution": "1. Đổi đơn vị vận tốc:\\n$$v = 72\\,\\text{km/h} = \\frac{72}{3.6} = 20\\,\\text{m/s}$$\\n\\n2. Chiếu định luật II Newton lên hai phương:\\n- Phương thẳng đứng (xe không chuyển động theo phương đứng):\\n$$N \\cos\\alpha = P = mg \\implies N = \\frac{mg}{\\cos\\alpha}$$\\n- Phương ngang hướng tâm:\\n$$F_n = N \\sin\\alpha = m \\frac{v^2}{R}$$\\n\\n3. Chia hai phương trình vế theo vế:\\n$$\\frac{N \\sin\\alpha}{N \\cos\\alpha} = \\frac{m v^2 / R}{mg} \\implies \\tan\\alpha = \\frac{v^2}{g R}$$\\n\\n4. Thay số tính toán:\\n$$\\tan\\alpha = \\frac{20^2}{9.8 \\times 200} = \\frac{400}{1960} \\approx 0.20408$$\\n$$\\alpha = \\arctan(0.20408) \\approx 11.53^\\circ$$\\n(Nhận xét: Góc nghiêng $\\alpha$ hoàn toàn không phụ thuộc vào khối lượng $m$ của ô tô; xe tải nặng hay xe con đều vào cua an toàn như nhau ở tốc độ thiết kế này)."
        },
        {
            "title": "Ví dụ 2: Khảo sát chuyển động của hệ hai vật nối qua ròng rọc (Máy Atwood)",
            "problem": "Hai quả nặng có khối lượng $m_1 = 3\\,\\text{kg}$ và $m_2 = 2\\,\\text{kg}$ ($m_1 > m_2$) được nối với nhau bằng một sợi dây nhẹ không co dãn vắt qua một ròng rọc cố định không khối lượng và không ma sát. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính gia tốc chuyển động của hệ và lực căng của sợi dây.",
            "analysis": "Do dây nhẹ không dãn nên hai vật có cùng độ lớn gia tốc $a_1 = a_2 = a$ và lực căng dây ở hai nhánh có cùng độ lớn $T_1 = T_2 = T$. Vật $m_1$ đi xuống và vật $m_2$ đi lên.",
            "solution": "1. Viết định luật II Newton cho từng vật:\\n- Vật 1 (chọn chiều dương hướng xuống):\\n$$m_1 g - T = m_1 a \\quad (1)$$\\n- Vật 2 (chọn chiều dương hướng lên):\\n$$T - m_2 g = m_2 a \\quad (2)$$\\n\\n2. Cộng (1) và (2) để khử $T$:\\n$$(m_1 - m_2) g = (m_1 + m_2) a \\implies a = \\frac{m_1 - m_2}{m_1 + m_2} g$$\\nThay số:\\n$$a = \\frac{3 - 2}{3 + 2} \\times 9.8 = \\frac{1}{5} \\times 9.8 = 1.96\\,\\text{m/s}^2$$\\n\\n3. Thay gia tốc $a$ vào (2) để tìm lực căng dây $T$:\\n$$T = m_2(g + a) = 2 \\times (9.8 + 1.96) = 2 \\times 11.76 = 23.52\\,\\text{N}$$\\n(Hoặc dùng công thức $T = \\frac{2 m_1 m_2}{m_1 + m_2} g = \\frac{2 \\times 3 \\times 2}{5} \\times 9.8 = 23.52\\,\\text{N}$)."
        }
    ],
    "pitfalls": [
        {
            "error": "Mặc định ngầm hiểu phản lực pháp tuyến luôn bằng trọng lượng: N = mg",
            "fix": "Phản lực $N$ chỉ bằng $mg$ khi vật nằm trên mặt ngang và không có lực kéo/đẩy xiên. Trên mặt phẳng nghiêng góc $\\alpha$, $N = mg\\cos\\alpha$. Nếu có lực kéo xiên góc $\\theta$, $N = mg - F\\sin\\theta$.",
            "tip": "Luôn luôn viết phương trình hình chiếu trên trục thẳng đứng vuông góc mặt tiếp xúc $\\sum F_y = 0$ để tìm biểu thức chính xác của $N$."
        },
        {
            "error": "Vẽ lực quán tính vào bài toán khi đang xét trong hệ quy chiếu quán tính (mặt đất)",
            "fix": "Lực quán tính chỉ tồn tại và được phép đưa vào phương trình khi người giải đứng trong hệ quy chiếu phi quán tính (có gia tốc). Nếu đứng ở mặt đất quan sát ô tô cua, không có lực ly tâm nào cả mà chỉ có lực ma sát đóng vai trò lực hướng tâm.",
            "tip": "Chọn trước một hệ quy chiếu và kiên định với nó: Nếu chọn hệ quán tính $\\to$ chỉ vẽ các lực thực; nếu chọn hệ gắn với vật gia tốc $\\to$ vẽ thêm lực quán tính."
        },
        {
            "error": "Áp dụng công thức ma sát trượt F_ms = μN cho vật đang đứng yên",
            "fix": "Khi vật đứng yên, lực ma sát là ma sát nghỉ: $F_{msn} \\le \\mu_s N$. Độ lớn của nó bằng đúng ngoại lực kéo dọc mặt tiếp xúc chứ không bằng $\\mu N$.",
            "tip": "Chỉ khi ngoại lực $F_{keo} > \\mu_s N$ thì vật mới bắt đầu trượt và khi đó mới được dùng $F_{mst} = \\mu_k N$."
        }
    ],
    "exercises": [
        {
            "id": "ex_2_1",
            "type": "easy",
            "q": "Một lực kéo nằm ngang không đổi $F = 50\\,\\text{N}$ tác dụng lên một khối gỗ có khối lượng $m = 10\\,\\text{kg}$ đang nằm yên trên mặt sàn nhẵn nằm ngang (bỏ qua mọi ma sát). Hãy tính gia tốc chuyển động của khối gỗ.",
            "unit": "m/s²",
            "ans": 5.0,
            "tol": 0.05,
            "hints": [
                "Áp dụng trực tiếp định luật II Newton cho phương nằm ngang: $F = ma$.",
                "Suy ra gia tốc $a = F / m$."
            ],
            "solution": "Theo định luật II Newton, gia tốc của khối gỗ là:\\n$$a = \\frac{F}{m} = \\frac{50}{10} = 5.0\\,\\text{m/s}^2$$\\nĐáp số: 5.0 m/s²"
        },
        {
            "id": "ex_2_2",
            "type": "easy",
            "q": "Treo một vật nặng thẳng đứng vào một lò xo có độ cứng $k = 200\\,\\text{N/m}$. Khi vật ở vị trí cân bằng, lò xo dãn ra một đoạn $\\Delta l = 4\\,\\text{cm} = 0.04\\,\\text{m}$. Lấy gia tốc trọng trường $g = 9.8\\,\\text{m/s}^2$. Hãy tính khối lượng của vật treo (làm tròn đến 2 chữ số thập phân).",
            "unit": "kg",
            "ans": 0.82,
            "tol": 0.05,
            "hints": [
                "Tại vị trí cân bằng, lực đàn hồi của lò xo cân bằng với trọng lực của vật: $F_{dh} = P$.",
                "Áp dụng định luật Hooke: $k \\Delta l = mg \\implies m = \\frac{k \\Delta l}{g}$."
            ],
            "solution": "Điều kiện cân bằng tĩnh của vật treo:\\n$$F_{dh} = P \\iff k \\Delta l = mg$$\\nKhối lượng của vật:\\n$$m = \\frac{k \\Delta l}{g} = \\frac{200 \\times 0.04}{9.8} = \\frac{8}{9.8} \\approx 0.8163 \\approx 0.82\\,\\text{kg}$$\\nĐáp số: 0.82 kg"
        },
        {
            "id": "ex_2_3",
            "type": "easy",
            "q": "Một kiện hàng có khối lượng $m = 5\\,\\text{kg}$ được kéo trượt trên sàn nằm ngang bởi một lực kéo nằm ngang $F = 25\\,\\text{N}$. Hệ số ma sát trượt giữa kiện hàng và mặt sàn là $\\mu = 0.2$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính gia tốc của kiện hàng.",
            "unit": "m/s²",
            "ans": 3.04,
            "tol": 0.05,
            "hints": [
                "Tính phản lực pháp tuyến $N = mg$.",
                "Tính lực ma sát trượt $F_{ms} = \\mu N$.",
                "Hợp lực tác dụng theo phương ngang là $F_{hl} = F - F_{ms} = ma$."
            ],
            "solution": "1. Phản lực của sàn lên vật:\\n$$N = mg = 5 \\times 9.8 = 49\\,\\text{N}$$\\n2. Lực ma sát trượt:\\n$$F_{ms} = \\mu N = 0.2 \\times 49 = 9.8\\,\\text{N}$$\\n3. Gia tốc của kiện hàng theo định luật II Newton:\\n$$a = \\frac{F - F_{ms}}{m} = \\frac{25 - 9.8}{5} = \\frac{15.2}{5} = 3.04\\,\\text{m/s}^2$$\\nĐáp số: 3.04 m/s²"
        },
        {
            "id": "ex_2_4",
            "type": "easy",
            "q": "Một hòn bi nhỏ khối lượng $m = 0.2\\,\\text{kg}$ được buộc vào đầu một sợi dây nhẹ dài $R = 0.8\\,\\text{m}$, đầu kia giữ cố định. Hòn bi quay tròn đều trên mặt bàn nằm ngang nhẵn không ma sát với tốc độ $v = 4\\,\\text{m/s}$. Lực căng của sợi dây bằng bao nhiêu Newton?",
            "unit": "N",
            "ans": 4.0,
            "tol": 0.05,
            "hints": [
                "Lực căng dây đóng vai trò lực hướng tâm duy nhất trên mặt bàn ngang: $T = F_n$.",
                "Công thức lực hướng tâm: $T = m \\frac{v^2}{R}$."
            ],
            "solution": "Lực căng của sợi dây cung cấp gia tốc hướng tâm cho chuyển động tròn đều:\\n$$T = F_n = m \\frac{v^2}{R} = 0.2 \\times \\frac{4^2}{0.8} = 0.2 \\times \\frac{16}{0.8} = 0.2 \\times 20 = 4.0\\,\\text{N}$$\\nĐáp số: 4.0 N"
        },
        {
            "id": "ex_2_5",
            "type": "mid",
            "q": "Một khối vật có khối lượng $m = 4\\,\\text{kg}$ trượt từ trên đỉnh xuống một mặt phẳng nghiêng góc $\\alpha = 30^\\circ$ so với phương ngang. Hệ số ma sát trượt giữa vật và mặt nghiêng là $\\mu = 0.15$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính gia tốc trượt của vật (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s²",
            "ans": 3.63,
            "tol": 0.1,
            "hints": [
                "Phân tích trọng lực thành hai thành phần: Song song mặt dốc $P_x = mg\\sin\\alpha$ và vuông góc mặt dốc $P_y = mg\\cos\\alpha$.",
                "Phản lực pháp tuyến $N = mg\\cos\\alpha$. Lực ma sát $F_{ms} = \\mu mg\\cos\\alpha$.",
                "Áp dụng định luật II Newton: $a = g(\\sin\\alpha - \\mu\\cos\\alpha)$."
            ],
            "solution": "Chiếu định luật II Newton lên phương mặt dốc hướng xuống:\\n$$mg\\sin\\alpha - F_{ms} = ma \\implies mg\\sin\\alpha - \\mu mg\\cos\\alpha = ma$$\\n$$a = g(\\sin\\alpha - \\mu\\cos\\alpha)$$\\nThay số với $\\alpha = 30^\\circ$:\\n$$\\sin 30^\\circ = 0.5; \\quad \\cos 30^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.86603$$\\n$$a = 9.8 \\times (0.5 - 0.15 \\times 0.86603) = 9.8 \\times (0.5 - 0.1299) = 9.8 \\times 0.3701 \\approx 3.627 \\approx 3.63\\,\\text{m/s}^2$$\\nĐáp số: 3.63 m/s²"
        },
        {
            "id": "ex_2_6",
            "type": "mid",
            "q": "Trong máy Atwood, hai quả nặng có khối lượng $m_1 = 3\\,\\text{kg}$ và $m_2 = 2\\,\\text{kg}$ được nối bằng sợi dây nhẹ không dãn vắt qua ròng rọc cố định không khối lượng và không ma sát. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính độ lớn lực căng của sợi dây nối (làm tròn đến 2 chữ số thập phân).",
            "unit": "N",
            "ans": 23.52,
            "tol": 0.1,
            "hints": [
                "Gia tốc của hệ hai vật: $a = \\frac{m_1 - m_2}{m_1 + m_2} g$.",
                "Lực căng dây tính theo công thức: $T = \\frac{2 m_1 m_2}{m_1 + m_2} g$."
            ],
            "solution": "Áp dụng công thức giải tích cho máy Atwood:\\n$$T = \\frac{2 m_1 m_2}{m_1 + m_2} g$$\\nThay các giá trị $m_1 = 3\\,\\text{kg}, m_2 = 2\\,\\text{kg}, g = 9.8\\,\\text{m/s}^2$:\\n$$T = \\frac{2 \\times 3 \\times 2}{3 + 2} \\times 9.8 = \\frac{12}{5} \\times 9.8 = 2.4 \\times 9.8 = 23.52\\,\\text{N}$$\\nĐáp số: 23.52 N"
        },
        {
            "id": "ex_2_7",
            "type": "mid",
            "q": "Một người có khối lượng $m = 65\\,\\text{kg}$ đứng trên một chiếc cân bàn đặt trong cabin của một thang máy. Thang máy đang chuyển động đi lên chậm dần đều với gia tốc có độ lớn $a = 1.8\\,\\text{m/s}^2$. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính số chỉ của cân bàn (độ lớn lực nén lên mặt cân theo đơn vị Newton).",
            "unit": "N",
            "ans": 520.0,
            "tol": 1.0,
            "hints": [
                "Thang máy đi lên chậm dần đều, nghĩa là vectơ gia tốc hướng xuống dưới ($a_y = -a$).",
                "Trong hệ quy chiếu gắn với thang máy, lực quán tính hướng lên trên: $F_{qt} = ma$.",
                "Số chỉ của cân chính là phản lực pháp tuyến: $N = m(g - a)$."
            ],
            "solution": "Phân tích chuyển động:\\n- Thang máy đang đi lên nhưng chuyển động chậm dần đều $\\implies$ Vectơ gia tốc $\\vec{a}$ hướng thẳng đứng xuống dưới.\\n- Theo định luật II Newton chiếu lên phương thẳng đứng:\\n$$mg - N = ma \\implies N = m(g - a)$$\\nThay số:\\n$$N = 65 \\times (9.8 - 1.8) = 65 \\times 8.0 = 520\\,\\text{N}$$\\n(Người cảm thấy 'nhẹ hơn' bình thường, hiện tượng giảm trọng lượng).\\nĐáp số: 520 N"
        },
        {
            "id": "ex_2_8",
            "type": "mid",
            "q": "Một xe lượn đi qua điểm cao nhất của một vòng xiếc thẳng đứng có bán kính $R = 12\\,\\text{m}$. Lấy $g = 9.8\\,\\text{m/s}^2$. Tính tốc độ tối thiểu của xe lượn tại đỉnh vòng xiếc để xe không bị rơi khỏi đường ray (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s",
            "ans": 10.84,
            "tol": 0.1,
            "hints": [
                "Tại đỉnh vòng xiếc, cả trọng lực P và phản lực của đường ray N đều hướng thẳng đứng xuống dưới hướng về tâm vòng tròn: $P + N = m \\frac{v^2}{R}$.",
                "Điều kiện để xe vẫn còn tiếp xúc với ray mà không bị rơi là $N \\ge 0$.",
                "Tốc độ tối thiểu đạt được khi $N = 0 \\implies v_{min} = \\sqrt{g R}$."
            ],
            "solution": "Phương trình lực hướng tâm tại điểm cao nhất của vòng xiếc:\\n$$P + N = m \\frac{v^2}{R} \\implies mg + N = m \\frac{v^2}{R} \\implies N = m\\left(\\frac{v^2}{R} - g\\right)$$\\nĐể xe không rơi khỏi ray, ray phải ép lên bánh xe hoặc ít nhất $N \\ge 0$:\\n$$\\frac{v^2}{R} - g \\ge 0 \\implies v \\ge \\sqrt{g R}$$\\nTốc độ giới hạn tối thiểu:\\n$$v_{min} = \\sqrt{g R} = \\sqrt{9.8 \\times 12} = \\sqrt{117.6} \\approx 10.844 \\approx 10.84\\,\\text{m/s}$$\\nĐáp số: 10.84 m/s"
        },
        {
            "id": "ex_2_9",
            "type": "hard",
            "q": "Một hạt bụi nước mưa có khối lượng $m = 4 \\times 10^{-5}\\,\\text{kg}$ rơi từ trạng thái nghỉ dưới tác dụng của trọng lực ($g = 9.8\\,\\text{m/s}^2$) và lực cản không khí tỷ lệ với vận tốc $F_c = -k v$ với hệ số cản $k = 8 \\times 10^{-5}\\,\\text{kg/s}$. Hãy tính khoảng thời gian (giây) kể từ lúc bắt đầu rơi cho đến khi vận tốc của hạt đạt $95\\%$ vận tốc tới hạn $v_{lim}$ (làm tròn đến 2 chữ số thập phân).",
            "unit": "s",
            "ans": 1.50,
            "tol": 0.05,
            "hints": [
                "Vận tốc theo thời gian: $v(t) = v_{lim} \\left(1 - e^{-\\frac{k}{m}t}\\right)$.",
                "Khi $v(t) = 0.95 v_{lim}$, suy ra $1 - e^{-\\frac{k}{m}t} = 0.95 \\implies e^{-\\frac{k}{m}t} = 0.05$.",
                "Giải phương trình: $t = \\frac{m}{k} \\ln(1 / 0.05) = \\frac{m}{k} \\ln(20)$."
            ],
            "solution": "Quy luật vận tốc rơi trong môi trường có lực cản tỷ lệ bậc nhất:\\n$$v(t) = v_{lim} \\left(1 - e^{-\\frac{k}{m}t}\\right)$$\\nĐiều kiện $v(t) = 0.95 v_{lim}$ tương đương với:\\n$$1 - e^{-\\frac{k}{m}t} = 0.95 \\implies e^{-\\frac{k}{m}t} = 0.05 = \\frac{1}{20}$$\\nLấy logarit tự nhiên hai vế:\\n$$-\\frac{k}{m}t = \\ln\\left(\\frac{1}{20}\\right) = -\\ln(20) \\implies t = \\frac{m}{k} \\ln(20)$$\\nThay số:\\n$$\\frac{m}{k} = \\frac{4 \\times 10^{-5}}{8 \\times 10^{-5}} = 0.5\\,\\text{s}$$\\n$$\\ln(20) \\approx 2.99573$$\\n$$t = 0.5 \\times 2.99573 \\approx 1.4979 \\approx 1.50\\,\\text{s}$$\\nĐáp số: 1.50 s"
        },
        {
            "id": "ex_2_10",
            "type": "hard",
            "q": "Một khối nêm hình tam giác có góc nghiêng $\\alpha = 30^\\circ$ và khối lượng $M = 3\\,\\text{kg}$ đặt trên mặt sàn nằm ngang nhẵn bóng không ma sát. Một vật nhỏ khối lượng $m = 1\\,\\text{kg}$ được thả trượt không ma sát từ đỉnh nêm xuống. Lấy $g = 9.8\\,\\text{m/s}^2$. Hãy tính độ lớn gia tốc của nêm theo phương ngang (làm tròn đến 2 chữ số thập phân).",
            "unit": "m/s²",
            "ans": 1.31,
            "tol": 0.05,
            "hints": [
                "Xét phương nằm ngang: Hệ (nêm + vật) không chịu ngoại lực theo phương ngang nên khối tâm của hệ bảo toàn gia tốc theo phương ngang ($a_{Gx} = 0$).",
                "Hoặc viết định luật II Newton cho nêm $M$: $N' \\sin\\alpha = M a_M$, trong đó $N'$ là phản lực giữa vật và mặt nêm.",
                "Công thức gia tốc nêm trượt tự do: $a_M = \\frac{m g \\sin\\alpha \\cos\\alpha}{M + m \\sin^2\\alpha}$."
            ],
            "solution": "Thiết lập hệ phương trình động lực học:\\n- Nêm $M$ chỉ chuyển động ngang dưới tác dụng của thành phần nằm ngang của phản lực $N'$ do vật ép lên nêm:\\n$$N' \\sin\\alpha = M a_M \\quad (1)$$\\n- Trong hệ quy chiếu phi quán tính gắn với nêm (gia tốc $a_M$ sang trái), vật $m$ chịu thêm lực quán tính $F_{qt} = m a_M$ sang phải.\\nChiếu lên phương vuông góc với mặt nêm:\\n$$N' = m g \\cos\\alpha - m a_M \\sin\\alpha \\quad (2)$$\\n- Thay (2) vào (1):\\n$$(m g \\cos\\alpha - m a_M \\sin\\alpha) \\sin\\alpha = M a_M$$\\n$$m g \\sin\\alpha \\cos\\alpha = (M + m \\sin^2\\alpha) a_M \\implies a_M = \\frac{m g \\sin\\alpha \\cos\\alpha}{M + m \\sin^2\\alpha}$$\\nThay số với $\\alpha = 30^\\circ$, $\\sin 30^\\circ = 0.5$, $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.86603$:\\n$$m g \\sin\\alpha \\cos\\alpha = 1 \\times 9.8 \\times 0.5 \\times 0.86603 \\approx 4.2435$$\\n$$M + m \\sin^2\\alpha = 3 + 1 \\times (0.5)^2 = 3 + 0.25 = 3.25$$\\n$$a_M = \\frac{4.2435}{3.25} \\approx 1.3057 \\approx 1.31\\,\\text{m/s}^2$$\\nĐáp số: 1.31 m/s²"
        }
    ]
}

print("Chapter 2 data module ready.")
