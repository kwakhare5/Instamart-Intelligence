export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center p-24 bg-zinc-50 dark:bg-zinc-900">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-sans text-sm lg:flex">
        <h1 className="text-4xl font-bold text-zinc-800 dark:text-zinc-100 mb-8">
          Instamart Intelligence
        </h1>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 w-full max-w-5xl mt-8">
        <a href="/household" className="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-black hover:border-zinc-300 transition-colors">
          <h2 className="text-xl font-semibold mb-2">Household Profile</h2>
          <p className="text-zinc-500">View consumption patterns and composition.</p>
        </a>
        
        <a href="/predictions" className="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-black hover:border-zinc-300 transition-colors">
          <h2 className="text-xl font-semibold mb-2">Predictions</h2>
          <p className="text-zinc-500">Track depletion dates for your groceries.</p>
        </a>

        <a href="/recipes" className="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-black hover:border-zinc-300 transition-colors">
          <h2 className="text-xl font-semibold mb-2">Recipe Planner</h2>
          <p className="text-zinc-500">Plan meals based on your pantry stock.</p>
        </a>

        <a href="/price-alerts" className="p-6 rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-black hover:border-zinc-300 transition-colors">
          <h2 className="text-xl font-semibold mb-2">Price Alerts</h2>
          <p className="text-zinc-500">Monitor commodity prices and trends.</p>
        </a>
      </div>
    </main>
  );
}
