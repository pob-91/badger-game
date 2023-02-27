using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour
{
    #region Public

    public static GameController Instance;

    public GameObject GameOverText;
    public float ScrollSpeed = -1.5f;
    public bool GameOver;
    public Text ScoreText;

    #endregion

    #region Private

    private int _score;

    #endregion

    #region Loop

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        } 
        else if (Instance != this)
        {
            Destroy(gameObject);
        }
    }

    // Use this for initialization
    private void Start()
    {

    }

    // Update is called once per frame
    private void Update()
    {
        if (!GameOver) return;
        if (Input.GetMouseButton(0))
        {
            SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
        }
    }

    #endregion

    #region Public

    public void BirdDied()
    {
        GameOverText.SetActive(true);
        GameOver = true;
    }

    public void BirdScored()
    {
        if (GameOver) return;

        _score++;
        ScoreText.text = string.Format("Score: {0}", _score);
    }

    #endregion
}
