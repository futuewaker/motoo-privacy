# Motoo 隐私政策 · Privacy Policy

**生效日期 Effective date: 2026 年 10 月 2 日 · October 2, 2026**

线上版本：[Motoo 隐私政策](https://motoo-privacy.pages.dev/)

## 简体中文

感谢你使用 Motoo。本政策说明个人收藏、位置与全球／国家成就、账号、共享藏馆、云端 AI 命名和购买相关数据的处理方式。「本地优先」表示许多功能在设备上运行，并不表示全部数据都不离开设备。

### 一、个人内容与私人 iCloud 同步

拍摄、设备端 Vision 抠图、手动命名和个人回看可以在设备上完成。个人瞬间、照片／贴纸、Live Photo 资源、名称、收藏关系、日期、可用的位置坐标和个人档案保存在设备数据库中。当设备的 Apple 账户和 iCloud 条件允许时，App 使用 SwiftData 与私人 CloudKit 数据库在同一 Apple 账户的设备间同步；这不需要登录 Motoo 账号。同步受设备 iCloud 设置、网络和 Apple 服务可用性影响。

该私人 CloudKit 数据库由 Apple 提供，Motoo 开发者不能通过自己的 Supabase 后台读取其中的个人收藏。成就、AI 或共享功能仍有各自独立的服务器数据处理，不能据此理解为「所有个人使用均不向服务器传送数据」。小组件读取 App Group 中的本地收藏快照，不自行上传位置或成就数据。

### 二、位置信息与全球／国家成就

- **拍摄定位（可选）**：在你开启 App 的记录位置选项并授予系统定位权限后，Motoo 在拍摄页面使用定位，记录封存地点。请求的目标精度约为百米，但实际坐标精度受系统与授权设置影响，可能足以识别具体地点；目标精度不等同于匿名化。App 不为此请求后台持续定位。
- **导入照片的位置**：当你主动选择照片导入时，App 可能读取该照片已有的 EXIF GPS 坐标。这与实时定位权限不同；关闭系统定位或拍摄位置开关，不会自动删除所选照片原有的 GPS 信息，也不会删除已保存的位置。
- **个人保存与同步**：瞬间经纬度用于地图回看，并可能随该瞬间进入你的私人 iCloud 数据库，因此它们不一定只存在于本设备。
- **Apple 地理服务**：为了显示地图、解析国家／地区、查询附近地形或核对时区，App 可能将坐标或附近查询区域交给 Apple 的 Core Location／MapKit 服务。坐标的处理适用 Apple 的服务及隐私政策。
- **国家与全球成就云端记录**：登录 Motoo 后，封存瞬间时，App 可将由地点解析出的国家／地区代码（例如 CN、JP）、成就／识别类别、瞬间记录标识、封存时间、本地日期和共享成员数发送至 Supabase，并与账号标识关联。用途是国家收集、全球探索及其他成就进度、跨设备恢复和重复记录校验。国家代码属于粗略位置信息；成就请求不包含经纬度，也不上传完整个人照片作为成就记录。
- **触发条件与控制**：这类成就记录也可能发生在只保存到个人藏馆时，不以加入共享藏馆或同意云端 AI 命名为前提；没有可用地点时不发送国家代码。关闭云端 AI 命名只停止 AI 图片请求，不会停止已登录账号的成就事件。你可以不登录或退出 Motoo 账号以停止后续账号成就上传；若不希望导入照片提供地点，请选择没有 GPS 信息的照片，或先移除照片位置元数据。已存在的云端成就数据可通过账号删除流程或联系我们处理。

我们不使用位置或国家成就数据开展广告追踪，也不将其出售给数据经纪商。

### 三、可选的云端 AI 命名

云端 AI 命名默认关闭。首次使用前，App 说明数据用途并要求明确同意。启用后，拍摄或导入进入预览时，压缩后的主体图片和场景缩略图经 Supabase 转发至智谱 AI（GLM），用于生成名称、识别类别和精细识别结果。场景图片可能包含人物、文字、地点线索或背景；请只提交你有权处理的图片。设备端 Vision 抠图本身不依赖这一上传。

Motoo 使用账号标识（已登录时）、设备标识、图片摘要、请求状态和识别结果管理每日额度、重复请求及服务安全。图片摘要不等于匿名数据，可能与账号或设备关联。Motoo 的额度数据库保存摘要及必要结果，不以额度记录保存图片原件；图片仍会在 AI 请求过程中被服务商处理。

你可以拒绝授权并继续本地抠图、手动命名和封存，也可以在「设置 → 云端 AI 命名」关闭授权以停止后续 AI 图片请求。已经发送的请求不能撤回；第三方的日志、保存期限和其他处理规则受相应服务政策约束，我们不承诺第三方即时删除或绝不留存请求。

### 四、账号、共享藏馆与通知

Motoo 使用 Sign in with Apple 与 Supabase Auth 提供账号。我们处理 Apple 提供的账号标识、可用的姓名和电子邮箱（包括 Apple 隐藏邮箱）、会话及账号资料，用于登录和账号管理。姓名或邮箱可能只在首次授权时提供；你设置的昵称、头像也可用于共享成员展示。无需登录即可使用个人核心功能；共享、账号成就同步及会员权益关联等在线功能会使用账号。

当你主动创建、加入或向共享藏馆保存内容时，下列数据会进入 Supabase：藏馆名称、邀请与成员关系、作者标识、贴纸及缩略图、名称／说明、评论、点赞、活动及时间记录。共享 Live 回忆球还会上传相应照片和配对视频资源，文件可能包含拍摄时间等媒体元数据，画面本身也可能透露地点。共享内容按藏馆访问权限展示给成员；被邀请的人加入后可访问相关内容。成员保存或导出的副本不受我们直接控制。

你设置的云端头像保存在 Supabase Storage；设备推送 token 与账号关联，用于 Apple APNs 发送共享活动通知。拒绝通知不影响个人收藏，但不会自动停止共享数据同步。退出藏馆、隐藏或软删除内容，与立即物理清除服务器文件不同；需要删除账号或进一步清除相关数据时，请使用下文流程或联系我们。

### 五、购买与权益

订阅和 App 内购买由 Apple App Store 处理，我们不接收银行卡号或支付方式详情。Motoo 使用 Apple 验证的商品及交易／原始交易标识、购买及到期状态、交易时间与账号关联数据核验会员、恢复购买并防止重复或错误归属。奖励兑换还可能处理兑换记录、奖励权益和必要的账号关联信息。删除 Motoo 账号不等于取消 Apple 自动续订；请在 Apple 账户的订阅管理中取消。

### 六、服务商、存储地区与跨地区处理

- **Apple**：提供私人 iCloud／CloudKit、Sign in with Apple、App Store 购买、地图／地理服务和 APNs 通知。其数据处理和存储适用 [Apple 隐私政策](https://www.apple.com/legal/privacy/)。
- **Supabase**：提供 Motoo 的账号、共享内容存储、成就记录、权益核验和 AI 请求转发。当前项目数据库区域为日本东京（ap-northeast-1）；边缘函数、网络传输、备份及平台运维不应理解为仅限于该数据库区域。参见 [Supabase 隐私政策](https://supabase.com/privacy)。
- **智谱 AI**：处理经同意提交的图片和识别请求。参见 [智谱开放平台](https://open.bigmodel.cn/) 公布的适用隐私与服务条款；本政策不将其请求处理承诺为只发生在你的设备或 Supabase 数据库区域。
- **Cloudflare Pages**：托管本隐私政策网页，访问网页时可能处理 IP 地址、浏览器信息和必要访问日志。参见 [Cloudflare 隐私政策](https://www.cloudflare.com/privacypolicy/)。本页面不嵌入广告或第三方分析脚本。

由于上述服务与功能，相关信息可能在你所在国家／地区之外传输、存储或处理。我们使用传输加密、访问控制及账号／藏馆权限限制访问；网络或云服务不代表绝对安全。Motoo 不接入第三方广告或行为分析 SDK，不出售或出租个人信息，不将功能数据用于跨 App 广告追踪。

服务请求可能产生必要的运行和安全日志，例如 IP 地址、请求时间、响应／错误状态及账号或设备上下文，用于排障、服务可用性和防滥用。这些日志不是广告分析；平台日志和备份的保存与清除受到服务商机制约束。

### 七、保存期限与删除范围

- **个人设备／iCloud 内容**：保存到你删除相应记录或通过 Apple 管理该 App 的 iCloud 数据。卸载 App 不能保证删除私人 iCloud、Supabase、其他设备或成员已保存的副本。
- **账号、成就、权益及共享记录**：按提供相关功能所需保存；目前成就事件没有独立的短期自动过期规则。退出账号、撤销定位或关闭 AI 不会自动删除既有记录。共享内容软删除可能保留数据库行或文件，供同步一致性和删除流程处理。
- **AI 额度明细**：当前 Motoo 服务端按清理任务保留最近约 7 天的图片摘要／额度明细；这不表示成就、共享内容或第三方 AI 日志也只有 7 天。
- **账号删除**：在「设置」的账号区域进入「删除账号」，按提示重新验证 Apple 身份并完成流程。服务器处理你的账号、本人共享内容／头像、评论／点赞、成就、关联权益和已识别归属于账号的额度数据，撤销相关登录授权。仍有其他成员的藏馆会转交合适成员，其他成员内容不会随你账号一并删除；仅剩你一人的共享藏馆按删除流程清理。App 显示完成前，请保持或重新打开 App 继续流程；关闭 App 可能暂停处理。
- **删除后仍需单独管理的内容**：私人设备／iCloud 收藏没有可靠的 Motoo 账号归属，账号删除不会自动抹除它们；你需要在 App 或 Apple iCloud 设置中管理。未关联账号的设备额度记录按其清理规则处理。必要的平台日志／备份也不保证与账号删除同时消失。
- **删除完成凭据**：为让请求超时或离线设备能确认完成，我们保留不含已删内容及 Apple 凭证的最小回执（随机请求标识、账号标识、校验摘要、状态与时间）。所有设备回执确认满 30 天后，在后续回执访问时清理；未确认的最小回执可能保留更久，以允许恢复。

### 八、你的选择、请求与设备权限

相机用于拍摄；照片权限／系统照片选择器用于导入或导出；可选的定位用于拍摄地点；可选的通知用于共享活动提醒。你可以在 iOS 设置管理这些权限。撤销权限主要停止后续访问，不清除此前导入或保存的数据。

你可以在 App 内删除个人内容、退出账号或共享藏馆、关闭云端 AI 命名，并在 Apple 设置管理 iCloud 与订阅。若要访问、更正、导出或删除我们服务器上与你有关的数据，或对跨地区处理提出问题，请发送邮件至 caiyuxuanjcgs@126.com。我们会核验必要的账号归属后处理；请勿发送密码或完整支付信息。

### 九、儿童与政策更新

Motoo 不面向 13 周岁以下儿童。如发现未成年人信息被不当提交，请联系我们处理。我们可能更新本政策，并在本页注明生效日期；涉及重要处理变化时会按适用要求提供通知或取得必要同意。

### 十、联系我们

Motoo 开发者联系邮箱：[caiyuxuanjcgs@126.com](mailto:caiyuxuanjcgs@126.com)。

## English

This policy describes personal collections, location and world/country achievements, accounts, shared collections, cloud AI naming and purchases. Local-first means many features run on your device; it does not mean that all data stays on that device.

### 1. Personal content and private iCloud sync

Capture, on-device Vision cutouts, manual naming and personal browsing can run locally. Your device database stores moments, photos/stickers, Live Photo resources, names, collection relationships, dates, available coordinates and profile data. When your Apple account and iCloud are available, SwiftData and private CloudKit sync this content between devices using that Apple account, independently of Motoo sign-in. Sync depends on device iCloud settings, connectivity and Apple's availability.

Apple provides this private database. The Motoo developer cannot read its personal collections through the Motoo Supabase backend. Achievements, AI and sharing have separate server processing described below. Widgets read local App Group snapshots and do not independently upload location or achievement data.

### 2. Location and world/country achievements

- **Optional camera location:** when you enable location recording and grant system permission, Motoo uses location on the capture screen to save a moment's place. The requested accuracy is approximately 100 metres, but actual coordinates depend on system settings and may identify a specific place. Requested accuracy is not anonymisation. Motoo does not request continuous background location for this feature.
- **Imported photo location:** photos you select may contain EXIF GPS coordinates, which Motoo can read. This is separate from live location permission. Disabling location permission or the camera location option neither removes existing photo GPS metadata nor deletes saved coordinates.
- **Personal storage:** coordinates support map review and can sync with their moment into your private iCloud database; they are not necessarily confined to one device.
- **Apple geographic services:** map display, country lookup, nearby terrain searches and time-zone checks may send coordinates or a search region to Apple's Core Location/MapKit services, subject to Apple's policies.
- **Server achievement records:** when signed into Motoo, saving a moment can send its derived country/region code (such as CN or JP), achievement/recognition category, capture identifier, capture time, local date and shared-member count to Supabase, linked to your account. This supports country collection, world exploration and other achievement progress, cross-device recovery and duplicate checks. Country codes are coarse location. The achievement request contains neither latitude/longitude nor a full personal photo.
- **Triggers and choices:** these events can also occur for saves to personal collections, independently of joining a shared collection or consenting to cloud AI naming. No country code is sent when no location is available. Disabling AI naming stops AI image requests, not signed-in achievement events. Remain signed out or sign out to stop future account achievement uploads. To avoid location from imports, select photos without GPS metadata or remove their location metadata first. Use account deletion or contact us for existing server achievement records.

Motoo does not use location or country achievements for advertising tracking or sell them to data brokers.

### 3. Optional cloud AI naming

Cloud AI naming is off by default and requires explicit consent after an explanation. When enabled, entering a capture/import preview sends compressed subject and scene images through Supabase to Zhipu AI (GLM) for names, categories and detailed recognition. Scene images may contain people, text, location clues or background details. Submit only images you are entitled to process. On-device Vision cutouts do not require this upload.

Account identifiers when signed in, device identifiers, image hashes, request status and recognition results support daily limits, duplicate checks and security. Hashes may remain linked to an account or device and are not necessarily anonymous. Motoo's quota database stores hashes and necessary results rather than original images; AI providers still process images during the request.

You can decline and continue local cutouts, manual naming and saving. Disable cloud AI naming in Settings to stop future AI image requests. Sent requests cannot be recalled. Provider retention and processing are subject to the applicable service policies; we do not promise immediate provider deletion or zero request retention.

### 4. Accounts, shared collections and notifications

Sign in with Apple and Supabase Auth provide Motoo accounts. Apple account identifiers, available names and email addresses (including relay addresses), sessions and profile information support authentication and account management. Apple may provide name/email only on first authorisation. Your chosen nickname and avatar may identify you to collection members. Personal core features work without sign-in; sharing, account achievement sync and membership association use accounts.

Creating, joining or saving to a shared collection sends collection names, invitation/member relationships, author identifiers, stickers/thumbnails, captions, comments, likes, activities and timestamps to Supabase. Shared Live memory orbs also upload the relevant photo and paired-video resources; files may contain capture-time and other media metadata, and images themselves may reveal places. Members can view content under collection access permissions, including invitees after joining. Copies saved or exported by members are outside our direct control.

Cloud avatars use Supabase Storage. Account-linked device push tokens support Apple APNs shared-activity notifications. Declining notifications does not stop shared-data sync. Leaving a collection, hiding or soft-deleting content is different from immediate physical removal of server files. For account removal or further deletion, use the process below or contact us.

### 5. Purchases and entitlements

Apple App Store handles subscriptions and in-app purchases. Motoo does not receive card numbers or payment-method details. Apple-verified product and transaction/original-transaction identifiers, purchase/expiry status, transaction times and account associations support membership verification, purchase restoration and ownership checks. Reward redemption may process redemption records, reward entitlements and necessary account associations. Deleting a Motoo account does not cancel an Apple subscription; cancel through your Apple account's subscription settings.

### 6. Providers, regions and international processing

- **Apple:** private iCloud/CloudKit, Sign in with Apple, App Store, geographic/map services and APNs. See [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).
- **Supabase:** Motoo authentication, shared storage, achievements, entitlement verification and AI request forwarding. The current project database region is Tokyo, Japan (ap-northeast-1). Edge execution, transit, backups and platform operations should not be assumed to stay exclusively within that database region. See [Supabase's Privacy Policy](https://supabase.com/privacy).
- **Zhipu AI:** consented images and recognition requests. See the applicable privacy/service terms published on the [Zhipu Open Platform](https://open.bigmodel.cn/). Processing is not promised to occur only on your device or in the Supabase database region.
- **Cloudflare Pages:** hosts this policy website and may process IP addresses, browser details and necessary access logs. See [Cloudflare's Privacy Policy](https://www.cloudflare.com/privacypolicy/). This page embeds no advertising or third-party analytics scripts.

These services may transmit, store or process information outside your country/region. We use encrypted transport, access controls and account/collection permissions. Network or cloud services cannot guarantee absolute security. Motoo uses no third-party advertising or behavioural analytics SDKs, does not sell or rent personal information and does not use feature data for cross-app advertising tracking.

Necessary operational/security logs may include IP address, request time, response/error status and account/device context for troubleshooting, availability and abuse prevention. These are not advertising analytics. Provider log and backup retention follows the relevant platform mechanisms.

### 7. Retention and deletion scope

- **Device/iCloud content:** retained until you delete the relevant records or manage the app's iCloud data through Apple. Uninstalling does not guarantee deletion of iCloud, Supabase, other-device or member-saved copies.
- **Account, achievements, entitlements and shared records:** retained as needed to provide their functions. Achievement events currently have no separate short-term automatic expiry. Sign-out, revoking location or disabling AI does not delete existing records. Soft-deleted shared content may leave rows/files for sync consistency and deletion processing.
- **AI quota details:** current Motoo cleanup retains approximately the most recent seven days of image-hash/quota details. This is not a seven-day limit for achievements, shared content or provider AI logs.
- **Account deletion:** choose Delete Account in the account area of Settings, reverify your Apple identity and complete the flow. The server processes your account, your shared content/avatar, comments/likes, achievements, associated entitlements and quota records identified as belonging to the account, and revokes related login authorisation. Collections with other members transfer to an eligible member; other members' content survives. Collections where you are the last member are cleaned up. Keep or reopen the app to continue until completion is shown; closing it may pause processing.
- **Separate data management:** private device/iCloud collections have no reliable Motoo-account ownership and are not automatically erased by account deletion. Manage them in the app or Apple iCloud settings. Unlinked device-only quota records follow their cleanup rules. Necessary provider logs/backups are not guaranteed to disappear at the same time.
- **Completion receipts:** minimal receipts without deleted content or Apple credentials retain random request identifiers, account identifiers, verification digests, state and timestamps so offline devices or timed-out requests can confirm completion. Once all device capabilities have been acknowledged for 30 days, subsequent receipt access triggers cleanup; unacknowledged minimal receipts may remain longer for recovery.

### 8. Choices, requests and device permissions

Camera supports capture; Photos permission/system picker supports import/export; optional Location supports capture places; optional Notifications supports shared activity. Manage permissions in iOS Settings. Revocation mainly stops future access and does not erase previously imported or saved data.

Delete personal content, sign out or leave shared collections, and disable cloud AI naming in the app. Manage iCloud and subscriptions through Apple. To request access, correction, export or deletion of server data, or ask about international processing, contact caiyuxuanjcgs@126.com. We verify necessary account ownership before processing requests. Do not send passwords or full payment details.

### 9. Children and policy changes

Motoo is not directed at children under 13. Contact us if a child's information has been submitted improperly. Updates are dated on this page; material processing changes receive notice or necessary consent as applicable.

### 10. Contact

Contact the Motoo developer at [caiyuxuanjcgs@126.com](mailto:caiyuxuanjcgs@126.com).
