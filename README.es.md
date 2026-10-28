# Web del Computer Vision and Robotics Lab — publicación en GitHub Pages

Guía en español para subir esta web a GitHub, publicarla con GitHub Pages y apuntar a
ella un dominio propio. Para la estructura del contenido (dónde se edita cada página,
cómo añadir personas o publicaciones) consulta el [README en inglés](README.md).

La web está hecha con [Hugo](https://gohugo.io) y el [kit de HugoBlox](https://github.com/HugoBlox/kit).
No hay que subir la web ya generada: se sube el código fuente y GitHub Actions la
compila y la publica cada vez que se hace `push` a la rama `main`.

---

## 1. Requisitos previos

- Una cuenta de GitHub (y, si la web va a ser del laboratorio, una **organización**
  de GitHub, p. ej. `cvr-lab`).
- `git` instalado en local.
- Para probar en local antes de subir (opcional pero recomendable):
  Hugo **extended 0.161.1**, Go y Node.js 22 con `pnpm` o `npm`.

```sh
pnpm install     # o: npm install
hugo server      # abre http://localhost:1313/
```

> No uses Hugo 0.162.0: falla con este módulo de HugoBlox (ver el README en inglés).
> La versión que usa la integración continua está fijada en `hugoblox.yaml`
> (`build.hugo_version`).

---

## 2. Elegir el nombre del repositorio

El nombre del repositorio decide la URL por defecto de la web:

| Nombre del repositorio | URL resultante |
| --- | --- |
| `<cuenta>.github.io` (p. ej. `cvr-lab.github.io`) | `https://cvr-lab.github.io/` |
| Cualquier otro (p. ej. `web`) | `https://cvr-lab.github.io/web/` |

Este proyecto está preparado para la primera opción: `go.mod` declara el módulo
`github.com/cvr-lab/cvr-lab.github.io` y `config/_default/hugo.yaml` tiene
`baseURL: 'https://cvr-lab.github.io/'`. Si usas otra cuenta u otro nombre:

1. Cambia `baseURL` en `config/_default/hugo.yaml` a la nueva URL.
2. (Opcional, solo por coherencia) cambia la línea `module` de `go.mod`.

El workflow de despliegue sobrescribe `baseURL` con la URL real que le da GitHub Pages
(`hugo --baseURL "${{ steps.pages.outputs.base_url }}/"` en `.github/workflows/build.yml`),
así que aunque se te olvide, la web publicada tendrá los enlaces bien. Aun así conviene
dejarlo correcto para que el servidor local y el `sitemap.xml` coincidan.

---

## 3. Crear el repositorio y subir el código

1. En GitHub: **New repository** (dentro de la organización si procede).
   - Nombre: `cvr-lab.github.io` (o el que hayas elegido).
   - Visibilidad: **Public**. GitHub Pages en repositorios privados requiere un plan
     de pago (GitHub Pro, Team o Enterprise).
   - **No** marques "Add a README", ".gitignore" ni licencia: el repositorio local ya
     los tiene y se produciría un conflicto en el primer `push`.

2. En local, desde la carpeta del proyecto:

   ```sh
   git add -A
   git commit -m "Primera versión de la web"
   git branch -M main
   git remote add origin git@github.com:cvr-lab/cvr-lab.github.io.git
   # o por HTTPS: https://github.com/cvr-lab/cvr-lab.github.io.git
   git push -u origin main
   ```

   El `.gitignore` ya excluye lo que no debe subirse: `public/` (web generada),
   `resources/` (caché de Hugo), `node_modules/`, `hugo_stats.json`, etc.

---

## 4. Activar GitHub Pages

Solo hay que hacerlo una vez por repositorio:

1. **Settings → Pages**.
2. En **Build and deployment → Source**, selecciona **GitHub Actions**
   (no "Deploy from a branch").
3. Ve a la pestaña **Actions**. Si el primer `push` se hizo antes de este paso, el
   despliegue habrá fallado: abre el workflow **Deploy website to GitHub Pages** y
   pulsa **Re-run all jobs** (o **Run workflow**, que también está habilitado).

Cuando termine, la URL aparece en **Settings → Pages** y en el resumen del workflow.

### Qué hace cada workflow

| Fichero | Cuándo se ejecuta | Qué hace |
| --- | --- | --- |
| `.github/workflows/deploy.yml` | `push` a `main` o manual | Lee `deploy.host` de `hugoblox.yaml` (debe ser `github-pages`), llama a `build.yml` y publica el resultado en Pages. |
| `.github/workflows/build.yml` | Pull requests a `main`, o llamado por `deploy.yml` | Instala Node, pnpm y Hugo, compila con `hugo --minify`, genera el índice de búsqueda con Pagefind y sube `public/` como artefacto. En un PR solo comprueba que la web compila. |
| `.github/workflows/upgrade.yml` | Lunes a las 05:00 UTC o manual | Abre un PR que actualiza los módulos de HugoBlox. |
| `.github/workflows/import-publications.yml` | `push` que cambie `publications.bib` | Convierte el BibTeX en páginas de `content/publications/` y abre un PR. |

Para que `upgrade.yml` e `import-publications.yml` puedan abrir pull requests, en
**Settings → Actions → General → Workflow permissions** marca
**Allow GitHub Actions to create and approve pull requests**. En una organización
puede que primero haya que permitirlo en los ajustes de la organización.

---

## 5. Flujo de trabajo diario

```sh
# editar contenido…
hugo server                 # revisar en local
git add -A
git commit -m "Añade noticia sobre X"
git push                    # a los ~2 minutos la web está actualizada
```

Para cambios grandes, trabaja en una rama y abre un pull request: `build.yml` compila
la web y avisa si algo se ha roto antes de fusionar.

---

## 6. Apuntar un dominio propio

Por defecto la web se sirve en `https://cvr-lab.github.io/`. Para servirla en un dominio
propio (p. ej. `cvrlab.es`, `www.cvrlab.es` o un subdominio institucional como
`cvrlab.ugr.es`) hay que tocar tres cosas: GitHub, el DNS del dominio y la
configuración de Hugo.

Documentación oficial:
- [Configuring a custom domain for your GitHub Pages site](https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Managing a custom domain](https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Verifying your custom domain](https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [Securing your site with HTTPS](https://docs.github.com/es/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
- [Troubleshooting custom domains](https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages)

### 6.1. Verificar el dominio (recomendado, antes de nada)

La verificación impide que otra cuenta de GitHub "secuestre" tu dominio si algún día
la web deja de estar publicada.

1. En la **organización** (o en tu cuenta personal): **Settings → Pages →
   Add a domain**, escribe el dominio (p. ej. `cvrlab.es`).
2. GitHub te da un registro **TXT** del estilo:

   | Tipo | Nombre | Valor |
   | --- | --- | --- |
   | TXT | `_github-pages-challenge-cvr-lab` | `abc123…` (el que te muestre GitHub) |

3. Créalo en el panel DNS del dominio, espera a que se propague y pulsa **Verify**.

### 6.2. Configurar el dominio en el repositorio

1. En el repositorio: **Settings → Pages → Custom domain**, escribe el dominio
   (p. ej. `www.cvrlab.es`) y pulsa **Save**.
2. Como el despliegue se hace con GitHub Actions, **no hace falta** un fichero
   `CNAME` en el repositorio: GitHub lo ignora en este modo y el dominio se guarda en
   los ajustes.

### 6.3. Registros DNS

Créalos en el panel de quien gestione el dominio (el registrador: DonDominio, OVH,
Cloudflare, IONOS, etc.). Elige el caso que corresponda.

**a) Subdominio (`www.cvrlab.es`, `cvrlab.ugr.es`, `lab.ejemplo.org`)** — un registro CNAME:

| Tipo | Nombre | Valor |
| --- | --- | --- |
| CNAME | `www` | `cvr-lab.github.io.` |

El valor es siempre `<cuenta>.github.io`, **sin** el nombre del repositorio.

**b) Dominio raíz o *apex* (`cvrlab.es`)** — registros A y AAAA a las IP de GitHub Pages:

| Tipo | Nombre | Valor |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

Si tu proveedor admite registros `ALIAS` o `ANAME` (o *CNAME flattening*, como
Cloudflare), puedes usar uno de ellos apuntando a `cvr-lab.github.io` en lugar de las IP.
Comprueba las IP vigentes en la
[documentación oficial](https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain)
por si cambian.

**c) Raíz y `www` a la vez (lo más habitual)** — crea los registros A/AAAA del caso (b)
**y** el CNAME `www` del caso (a). En GitHub configura como dominio personalizado el
que quieras como principal (p. ej. `www.cvrlab.es`); GitHub redirige automáticamente
el otro.

> No uses comodines (`*.cvrlab.es`) apuntando a GitHub: permiten que otros publiquen
> en tus subdominios.

### 6.4. Comprobar la propagación

Los cambios DNS pueden tardar desde minutos hasta 24–48 h:

```sh
dig www.cvrlab.es +noall +answer     # debe mostrar CNAME cvr-lab.github.io.
dig cvrlab.es +noall +answer         # debe mostrar las cuatro IP 185.199.10x.153
```

También puedes usar <https://dnschecker.org>.

### 6.5. Activar HTTPS

Cuando el DNS esté propagado, GitHub emite automáticamente un certificado de Let's
Encrypt (puede tardar hasta una hora). Después marca **Settings → Pages →
Enforce HTTPS**. Si la casilla está deshabilitada, el certificado aún no está listo;
quitar y volver a guardar el dominio personalizado suele forzar un nuevo intento.

Si usas Cloudflare con el proxy activado (nube naranja), pon el cifrado SSL/TLS en
**Full**, no en *Flexible*, para evitar bucles de redirección; o desactiva el proxy
(nube gris) y deja que GitHub gestione el certificado.

### 6.6. Actualizar la configuración de Hugo

Cambia `baseURL` en `config/_default/hugo.yaml` al dominio final:

```yaml
baseURL: 'https://www.cvrlab.es/'
```

y haz `push`. El workflow ya toma la URL de Pages automáticamente, pero así la
configuración local, el `sitemap.xml` y el RSS quedan coherentes.

### 6.7. Caso particular: un subdominio de la UGR

Si se quiere algo como `cvrlab.ugr.es`, el DNS de `ugr.es` no lo controla el
laboratorio. Hay que pedir al servicio de informática de la universidad (CSIRC) que
cree el registro:

```
cvrlab.ugr.es.   CNAME   cvr-lab.github.io.
```

y, si piden verificación, también el TXT del apartado 6.1. Después se siguen los
pasos 6.2, 6.5 y 6.6 con normalidad.

Para no romper enlaces antiguos, la web actual en `https://www.ugr.es/~cvrlab/` puede
sustituirse por una página que redirija a la nueva dirección:

```html
<!doctype html>
<meta http-equiv="refresh" content="0; url=https://cvr-lab.github.io/">
<link rel="canonical" href="https://cvr-lab.github.io/">
<p>La web se ha trasladado a <a href="https://cvr-lab.github.io/">cvr-lab.github.io</a>.</p>
```

(Sustituye la URL por el dominio final si se configura uno).

---

## 7. Problemas frecuentes

| Síntoma | Causa probable y solución |
| --- | --- |
| El workflow falla en *Deploy* con "Get Pages site failed" o 404 | Pages no está activado o la fuente no es **GitHub Actions** (apartado 4). |
| El despliegue falla con "Branch is not allowed to deploy to github-pages" | **Settings → Environments → github-pages**: añade `main` a las ramas permitidas. |
| La web carga sin estilos o con enlaces rotos | `baseURL` incorrecto, o repositorio que no se llama `<cuenta>.github.io` y la web vive en una subruta (apartado 2). |
| Falla *Build with Hugo* con `assignment to entry in nil map` | Se está usando Hugo 0.162.0; deja `hugoblox.yaml` en 0.161.1. |
| Falla con "Missing dependency '@tailwindcss/cli'" | Falta en `package.json`; ejecuta `pnpm add @tailwindcss/cli tailwindcss` y sube el cambio. |
| "Domain's DNS record could not be retrieved" o *Enforce HTTPS* deshabilitado | El DNS aún no se ha propagado o los registros están mal (apartados 6.3–6.4). |
| El dominio personalizado desaparece tras un despliegue | Solo pasa si se publica desde una rama sin fichero `CNAME`; con la fuente **GitHub Actions** el dominio se guarda en los ajustes y no debería ocurrir. Revisa el apartado 4. |
| Los workflows de actualización o de BibTeX no abren PR | Falta el permiso **Allow GitHub Actions to create and approve pull requests** (apartado 4). |
