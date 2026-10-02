# Motoo 隐私政策（静态站点）

Motoo App 的隐私政策静态页面，用于 App Store Connect 合规与 App 内付费墙链接。

## 页面

| 文件 | 用途 |
|---|---|
| `index.html` | 主页面（推荐作为隐私政策 URL） |
| `privacy.html` | 别名，自动跳转到 `index.html` |
| `policy.md` | 双语政策正文，后续修改从这里开始 |
| `build_site.py` | 使用原网页样式生成 HTML；只需 Python 3，无第三方依赖 |

## 维护现有线上页面

本仓库 `main` 分支已接入 Cloudflare Pages 的 `motoo-privacy` 项目，正式 URL 为 [https://motoo-privacy.pages.dev/](https://motoo-privacy.pages.dev/)。无需另建站点或更换 App 内 URL。

1. 修改 `policy.md`，保持中英文披露一致，更新生效日期。
2. 在本仓库执行 `python3 build_site.py`，生成 `index.html`，预览并核对内容。
3. 将同一份 `policy.md` 同步到 App 仓库的 `隐私政策.md`；数据流变化还需同步 App 的 `PrivacyInfo.xcprivacy` 与 App Store Connect 的隐私回答。
4. 提交本次政策相关文件并推送到 `main`。GitHub 提交的 **Cloudflare Pages** 检查成功后，访问正式 URL 核对日期和正文。

部署失败时，从 GitHub 提交的 Cloudflare Pages 检查链接进入现有项目排查。历史 Git 提交可用于恢复旧网页。`privacy.html` 保持重定向到主页面。

## Cloudflare Pages 部署

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
2. 选择 GitHub 账号，选中本仓库 **`motoo-privacy`**
3. 构建设置：
   - **Framework preset**：None
   - **Build command**：（留空）
   - **Build output directory**：`/`
4. 部署完成后，隐私政策 URL 通常为：

```
https://<你的-pages-项目名>.pages.dev/
```

若你绑定了自定义域名，例如：

```
https://motoo.app/privacy
```

## 填到哪里

部署成功后，把最终 HTTPS URL 填进：

1. `Motoo/Motoo/Configuration/AppConfig.swift` → `privacyPolicyURL`
2. App Store Connect → App → **App 隐私** / 商店信息中的隐私政策 URL

## 联系邮箱

`caiyuxuanjcgs@126.com`
