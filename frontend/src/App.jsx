import { useState } from 'react'
import QueryInput from './components/QueryInput'
import ResponseCard from './components/ResponseCard'

function App() {
  const [data, setData] = useState(null)

  const handleQuery = async (question) => {
    try {
      const res = await fetch('http://localhost:8000/query', { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      })

      const result = await res.json()
      setData(result)
    } catch (error) {
      setData({
        question,
        decided_data_source: 'unknown',
        format: 'text',
        response: '❌ Failed to reach backend.',
      })
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 p-4 flex flex-col items-center gap-6">
      <h1 className="text-3xl font-bold text-center mt-4">Natural Language Query App</h1>
      <QueryInput onSubmit={handleQuery} />
      {data && <ResponseCard data={data} />}
    </div>
  )
}

export default App
