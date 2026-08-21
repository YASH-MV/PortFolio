export default function Footer({
  name = "Yash Raj",
  links = [
    { label: "GitHub", href: "https://github.com/YASH-MV" },
    { label: "LinkedIn", href: "https://www.linkedin.com/in/yash-raj-b8798a285/" },
    { label: "Email", href: "mailto:yashraj64004@gmail.com" },
  ],
}) {
  return (
    <footer className="border-t border-base-border px-6 py-10">
      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 sm:flex-row">
        <p className="font-display text-xs text-ink-dim">
          © {new Date().getFullYear()} {name} · built with a RAG pipeline of its own
        </p>
        <div className="flex gap-6 font-display text-xs uppercase tracking-widest text-ink-muted">
          {links.map((l) => (
            <a key={l.label} href={l.href} className="transition-colors hover:text-spark-amber">
              {l.label}
            </a>
          ))}
        </div>
      </div>
    </footer>
  );
}
