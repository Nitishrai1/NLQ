function ResponseCard({ data }) {
  return (
    <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-xl">
      <h2 className="text-xl font-semibold mb-2">Response</h2>
      <p><span className="font-medium">🧠 Question:</span> {data.question}</p>
      <p><span className="font-medium">📦 Data Source:</span> {data.decided_data_source}</p>
      <p><span className="font-medium">🧾 Format:</span> {data.format}</p>
      <p className="mt-4 text-gray-800 border-t pt-2"><span className="font-medium">📤 Response:</span> {data.response}</p>
    </div>
  )
}

export default ResponseCard
