# Motoo 隐私政策（静态站点）

Motoo App 的隐私政策静态页面，用于 App Store Connect 合规与 App 内付费墙链接。

## 页面

| 文件 | 用途 |
|---|---|
| `index.html` | 主页面（推荐作为隐私政策 URL） |
| `privacy.html` | 别名，自动跳转到 `index.html` |

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
