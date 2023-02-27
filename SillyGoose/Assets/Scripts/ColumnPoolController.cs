using UnityEngine;

public class ColumnPoolController : MonoBehaviour
{
    #region Public

    public int ColumnPoolSize = 5;
    public GameObject ColumnPrefab;
    public float SpawnRate = 4f;
    public float ColumnMinY = -1f;
    public float ColumnMaxY = 3.5f;

    #endregion

    #region Private

    private GameObject[] _columns;
    private Vector2 _objectPoolPosition = new Vector2(-15f, -25f); // offscreen position
    private float _timeSinceLastSpawned = 4f;
    private readonly float _spawnX = 15f;
    private int _currentColumnIdx;

    #endregion

    #region Unity

    private void Start()
    {
        _columns = new GameObject[ColumnPoolSize];
        for (int i = 0; i < ColumnPoolSize; i++)
        {
            _columns[i] = Instantiate(ColumnPrefab, _objectPoolPosition, Quaternion.identity);
        }
    }

    private void Update()
    {
        if (GameController.Instance.GameOver) return;

        _timeSinceLastSpawned += Time.deltaTime;

        if (_timeSinceLastSpawned < SpawnRate) return;

        _timeSinceLastSpawned = 0f;

        var spawnY = Random.Range(ColumnMinY, ColumnMaxY);
        _columns[_currentColumnIdx].transform.position = new Vector2(_spawnX, spawnY);
        _currentColumnIdx++;
        if (_currentColumnIdx >= ColumnPoolSize)
        {
            _currentColumnIdx = 0;
        }
    }

    #endregion
}